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

####################################################################################################
# Global Constants
####################################################################################################

__openstack_user_template__ = {}
__openstack_user_template__['credentials'] = {}
__openstack_user_template__['credentials']['username'] = "your user name"
__openstack_user_template__['credentials']['password'] = "your user password"
__openstack_user_template__['project'] = "default"

__cf_manager_url__ = "10.12.0.132:8080"
__NON_FPGA_IDENTIFIER__ = "NON_FPGA"

__cfsp_username__ = 'gobal_username_example'
__cfsp_password__ = 'gobal_password_example'
__cfsp_project__  = 'default'

__POST_CLUSTER_TIMEOUT__   = 130
__GET_CLUSTER_TIMEOUT__    = 5
__DELETE_CLUSTER_TIMEOUT__ = 20

__GET_INSTANCE_TIMEOUT__    = 5
__DELETE_INSTANCE_TIMEOUT__ = 20
