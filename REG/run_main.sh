#!/bin/bash
#  *
#  *                       cloudFPGA
#  *     Copyright IBM Research, All Rights Reserved
#  *    =============================================
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

# @brief A function to check if previous step passed.
# @param[in] $1 the return value of the previous command.
function exit_on_error {
    if [ $1 -ne 0 ]; then
        echo "EXIT ON ERROR: Regression '$0' FAILED."
        echo "  Last return value was $1."
        exit $1
    fi
}

# STEP-0: We need to set the right environment
export rootDir="$cFSPRootDir/"  #the / is IMPORTANT

#also, we need a license:
export XILINXD_LICENSE_FILE=2100@pokwinlic1.pok.ibm.com:2100@pokwinlic2.pok.ibm.com:2100@pokwinlic3.pok.ibm.com


echo "Set cFp environment."
retval=1


#===============================================================================
# FUNCTION - fCleanUpAndExit - Clean up the environement and exit
#  @param[in]  $1 The code to return
#              
#  @returns    $1
#===============================================================================
fCleanUpAndExit() {
	echo -e "#"
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

cp test/user_example.json test/user.json

user=$(head -n 1 /tmp/zyc2-user-vpn.credentials)
pass=$(tail -n 1 /tmp/zyc2-user-vpn.credentials)
sed -i s/example_user/$user/ test/user.json
sed -i s/example_password/$pass/ test/user.json
cat zyc2-vpn/up-user
cat zyc2-vpn/zyc2-vpn-user.ovpn
sed -i s/user_example.json/user.json/ test/test_cF.py
    
    
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
echo "===   REGRESSION - START OF BUILD: 'monolithic' "
echo "===     $0"
echo "================================================================"
cd $rootDir/test
python3 test_cF.py
exit_on_error $? 
echo "================================================================"
echo "===   REGRESSION - END OF BUILD  : 'monolithic' "
echo "===     $0"
echo "================================================================"


fCleanUpAndExit $retval


