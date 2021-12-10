# coding: utf-8

"""
    cloudFPGA Resource Manager API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AdministrationPlatformLogicBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image_details': 'str',
        'dcp_file': 'str',
        'bit_file': 'str',
        'mcs_file': 'str',
        'sig_file': 'str',
        'pr_verify_rpt': 'str'
    }

    attribute_map = {
        'image_details': 'image_details',
        'dcp_file': 'dcp_file',
        'bit_file': 'bit_file',
        'mcs_file': 'mcs_file',
        'sig_file': 'sig_file',
        'pr_verify_rpt': 'pr_verify_rpt'
    }

    def __init__(self, image_details=None, dcp_file=None, bit_file=None, mcs_file=None, sig_file=None, pr_verify_rpt=None):  # noqa: E501
        """AdministrationPlatformLogicBody - a model defined in Swagger"""  # noqa: E501
        self._image_details = None
        self._dcp_file = None
        self._bit_file = None
        self._mcs_file = None
        self._sig_file = None
        self._pr_verify_rpt = None
        self.discriminator = None
        self.image_details = image_details
        self.dcp_file = dcp_file
        self.bit_file = bit_file
        self.mcs_file = mcs_file
        self.sig_file = sig_file
        self.pr_verify_rpt = pr_verify_rpt

    @property
    def image_details(self):
        """Gets the image_details of this AdministrationPlatformLogicBody.  # noqa: E501

        Must be a valid `image_detail` dict-representation. Example: ```json  {    \"fpga_board\": \"FMKU60\",    \"shell_type\": \"Themisto\",    \"version\":    \"0.9.42\",    \"needs_mantle\": false,    \"has_fmc_tcp\": true,    \"comment\" : \"Some valuable               information for humans (optional)\"  }  ```   # noqa: E501

        :return: The image_details of this AdministrationPlatformLogicBody.  # noqa: E501
        :rtype: str
        """
        return self._image_details

    @image_details.setter
    def image_details(self, image_details):
        """Sets the image_details of this AdministrationPlatformLogicBody.

        Must be a valid `image_detail` dict-representation. Example: ```json  {    \"fpga_board\": \"FMKU60\",    \"shell_type\": \"Themisto\",    \"version\":    \"0.9.42\",    \"needs_mantle\": false,    \"has_fmc_tcp\": true,    \"comment\" : \"Some valuable               information for humans (optional)\"  }  ```   # noqa: E501

        :param image_details: The image_details of this AdministrationPlatformLogicBody.  # noqa: E501
        :type: str
        """
        if image_details is None:
            raise ValueError("Invalid value for `image_details`, must not be `None`")  # noqa: E501

        self._image_details = image_details

    @property
    def dcp_file(self):
        """Gets the dcp_file of this AdministrationPlatformLogicBody.  # noqa: E501

        the STATIC dcp checkpoint to be used by users  # noqa: E501

        :return: The dcp_file of this AdministrationPlatformLogicBody.  # noqa: E501
        :rtype: str
        """
        return self._dcp_file

    @dcp_file.setter
    def dcp_file(self, dcp_file):
        """Sets the dcp_file of this AdministrationPlatformLogicBody.

        the STATIC dcp checkpoint to be used by users  # noqa: E501

        :param dcp_file: The dcp_file of this AdministrationPlatformLogicBody.  # noqa: E501
        :type: str
        """
        if dcp_file is None:
            raise ValueError("Invalid value for `dcp_file`, must not be `None`")  # noqa: E501

        self._dcp_file = dcp_file

    @property
    def bit_file(self):
        """Gets the bit_file of this AdministrationPlatformLogicBody.  # noqa: E501

        The corresponding static bitfile, to write to the FPGA  # noqa: E501

        :return: The bit_file of this AdministrationPlatformLogicBody.  # noqa: E501
        :rtype: str
        """
        return self._bit_file

    @bit_file.setter
    def bit_file(self, bit_file):
        """Sets the bit_file of this AdministrationPlatformLogicBody.

        The corresponding static bitfile, to write to the FPGA  # noqa: E501

        :param bit_file: The bit_file of this AdministrationPlatformLogicBody.  # noqa: E501
        :type: str
        """
        if bit_file is None:
            raise ValueError("Invalid value for `bit_file`, must not be `None`")  # noqa: E501

        self._bit_file = bit_file

    @property
    def mcs_file(self):
        """Gets the mcs_file of this AdministrationPlatformLogicBody.  # noqa: E501

        The corresponding mcs file, to write to the board flash  # noqa: E501

        :return: The mcs_file of this AdministrationPlatformLogicBody.  # noqa: E501
        :rtype: str
        """
        return self._mcs_file

    @mcs_file.setter
    def mcs_file(self, mcs_file):
        """Sets the mcs_file of this AdministrationPlatformLogicBody.

        The corresponding mcs file, to write to the board flash  # noqa: E501

        :param mcs_file: The mcs_file of this AdministrationPlatformLogicBody.  # noqa: E501
        :type: str
        """
        if mcs_file is None:
            raise ValueError("Invalid value for `mcs_file`, must not be `None`")  # noqa: E501

        self._mcs_file = mcs_file

    @property
    def sig_file(self):
        """Gets the sig_file of this AdministrationPlatformLogicBody.  # noqa: E501

        The corresponding .sig file of the binfile  # noqa: E501

        :return: The sig_file of this AdministrationPlatformLogicBody.  # noqa: E501
        :rtype: str
        """
        return self._sig_file

    @sig_file.setter
    def sig_file(self, sig_file):
        """Sets the sig_file of this AdministrationPlatformLogicBody.

        The corresponding .sig file of the binfile  # noqa: E501

        :param sig_file: The sig_file of this AdministrationPlatformLogicBody.  # noqa: E501
        :type: str
        """
        if sig_file is None:
            raise ValueError("Invalid value for `sig_file`, must not be `None`")  # noqa: E501

        self._sig_file = sig_file

    @property
    def pr_verify_rpt(self):
        """Gets the pr_verify_rpt of this AdministrationPlatformLogicBody.  # noqa: E501

        Result of the `pr_verify` command  # noqa: E501

        :return: The pr_verify_rpt of this AdministrationPlatformLogicBody.  # noqa: E501
        :rtype: str
        """
        return self._pr_verify_rpt

    @pr_verify_rpt.setter
    def pr_verify_rpt(self, pr_verify_rpt):
        """Sets the pr_verify_rpt of this AdministrationPlatformLogicBody.

        Result of the `pr_verify` command  # noqa: E501

        :param pr_verify_rpt: The pr_verify_rpt of this AdministrationPlatformLogicBody.  # noqa: E501
        :type: str
        """
        if pr_verify_rpt is None:
            raise ValueError("Invalid value for `pr_verify_rpt`, must not be `None`")  # noqa: E501

        self._pr_verify_rpt = pr_verify_rpt

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdministrationPlatformLogicBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdministrationPlatformLogicBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
