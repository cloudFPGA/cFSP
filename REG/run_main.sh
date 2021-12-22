#!/bin/bash
# *****************************************************************************
# *                            cloudFPGA
# *                Copyright 2016 -- 2022 IBM Corporation
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *     http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# *----------------------------------------------------------------------------
#
#  *     Created: Oct 2021
#  *     Authors: FAB, WEI, NGL, POL, DID
#  *
#  *     Description:
#  *        Main cFSP regressions script.
#  *
#  *     Details:
#  *       - This script is typically called the Jenkins server.
#  *       - It expects to be executed from the cFSP root directory.
#  *       - The '$cFSPRootDir' variable must be set externally. 
#  *       - All environment variables must be sourced beforehand.
#  *


# STEP-0: We need to set the right environment
export rootDir="$cFSPRootDir/"  #the / is IMPORTANT

echo "Set cFp environment."
retval=0

#===============================================================================
# FUNCTION - fCleanUpAndExit - Clean up the environement and exit
#  @param[in]  $1 The code to return
#              
#  @returns    $1
#===============================================================================
fCleanUpAndExit() {
    if [ $1 -ne 0 ]; then
        echo "EXIT ON ERROR: Regression '$0' FAILED."
        echo "  Last return value was $1."
    fi    
    
    echo -e "#"
    echo -e "# SUCCESSFULL TEST"
    echo -e "# CLEANING UP BEFORE EXITING"
    echo -e "#"  
    
    sudo kill $(cat /tmp/zyc2-user-vpn.pid)
    rm -f /tmp/zyc2-user-vpn.credentials
    rm -f /tmp/zyc2-user-vpn.conf

    exit $1
}



###############################################################################
#                                                                             #
#                                 MAIN                                        #
#                                                                             #
###############################################################################
id
echo -e "#"
echo -e "# Configuring OpenVPN"
echo -e "#"
cp -f ${ZYC2_USER_VPN_CONFIG} /tmp/zyc2-user-vpn.conf
cp -f ${ZYC2_USER_VPN_CREDENTIALS} /tmp/zyc2-user-vpn.credentials
sudo openvpn --config /tmp/zyc2-user-vpn.conf --auth-user-pass /tmp/zyc2-user-vpn.credentials --log /tmp/zyc2-user-vpn.log --writepid /tmp/zyc2-user-vpn.pid --daemon
sleep 10
ping -c 4 10.12.0.1
if [ $? -ne 0 ]; then echo -e "ERROR: Cannot ping the VPN"; exit 1; fi


echo -e "#"
echo -e "# SETTING UP CREDENTIALS FILE"
echo -e "#"
cp test/user_example.json test/user.json
user=$(head -n 1 /tmp/zyc2-user-vpn.credentials)
pass=$(tail -n 1 /tmp/zyc2-user-vpn.credentials)
sed -i s/example_user/$user/ test/user.json
sed -i s/example_password/$pass/ test/user.json
sed -i s/user_example.json/user.json/ test/test_cF.py
cat test/user.json
    
echo -e "#"
echo -e "# SETTING UP PYTHON VIRTUAL ENVIRONMENT"
echo -e "#"
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt


echo "================================================================"
echo "===   START OF REGRESSION:" 
echo "===     $0"
echo "================================================================"

echo "================================================================"
echo "===   REGRESSION - START OF BUILD: 'test_cF.py' "
echo "===     $0"
echo "================================================================"
cd $rootDir/test
python3 test_cF.py 
retval=$?

echo "================================================================"
echo "===   REGRESSION - END OF BUILD  : 'test_cF.py' "
echo "===     $0"
echo "================================================================"


fCleanUpAndExit $retval
