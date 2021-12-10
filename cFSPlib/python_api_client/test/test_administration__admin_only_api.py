# coding: utf-8

"""
    cloudFPGA Resource Manager API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.administration__admin_only_api import AdministrationAdminOnlyApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdministrationAdminOnlyApi(unittest.TestCase):
    """AdministrationAdminOnlyApi unit test stubs"""

    def setUp(self):
        self.api = AdministrationAdminOnlyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cf_manager_rest_api_admin_test_instance(self):
        """Test case for cf_manager_rest_api_admin_test_instance

        Test the instance **if not used**  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_admin_update_flash(self):
        """Test case for cf_manager_rest_api_admin_update_flash

        Update the flash of a resource **if not used**  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_delete_ippool(self):
        """Test case for cf_manager_rest_api_delete_ippool

        Remove a /24 subnet  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_get_all_composable_logic(self):
        """Test case for cf_manager_rest_api_get_all_composable_logic

        Get list of all composable logic  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_get_buildscripts_all(self):
        """Test case for cf_manager_rest_api_get_buildscripts_all

        Get all registered build script versions  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_get_ippool(self):
        """Test case for cf_manager_rest_api_get_ippool

        Get all ip addresses in the current pool  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_get_mantle_logic_all(self):
        """Test case for cf_manager_rest_api_get_mantle_logic_all

        Get all mantle logics  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_get_platform_logic_all(self):
        """Test case for cf_manager_rest_api_get_platform_logic_all

        Get all platform logics  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_get_single_buildscript(self):
        """Test case for cf_manager_rest_api_get_single_buildscript

        Get details of one registered build script  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_get_single_composable_logic(self):
        """Test case for cf_manager_rest_api_get_single_composable_logic

        Get details of one composable logic  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_post_buildscript(self):
        """Test case for cf_manager_rest_api_post_buildscript

        Register a new build script version  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_post_ippool(self):
        """Test case for cf_manager_rest_api_post_ippool

        Post a new `/24` ip pool (subnet)  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_post_mantle_logic(self):
        """Test case for cf_manager_rest_api_post_mantle_logic

        Upload a new dynamic platform logic  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_post_platform_logic(self):
        """Test case for cf_manager_rest_api_post_platform_logic

        Upload a new platform logic  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_put_buildscript(self):
        """Test case for cf_manager_rest_api_put_buildscript

        Update a registered build script  # noqa: E501
        """
        pass

    def test_cf_manager_rest_api_put_composable_logic_status(self):
        """Test case for cf_manager_rest_api_put_composable_logic_status

        Update status of a composable logic  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
