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

class InlineResponse200(object):
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
        'gateway': 'str',
        'ip_addr': 'str',
        'status': 'str',
        'subnet': 'str',
        'subnet_mask': 'str'
    }

    attribute_map = {
        'gateway': 'gateway',
        'ip_addr': 'ip_addr',
        'status': 'status',
        'subnet': 'subnet',
        'subnet_mask': 'subnet_mask'
    }

    def __init__(self, gateway=None, ip_addr=None, status=None, subnet=None, subnet_mask=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._gateway = None
        self._ip_addr = None
        self._status = None
        self._subnet = None
        self._subnet_mask = None
        self.discriminator = None
        if gateway is not None:
            self.gateway = gateway
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if status is not None:
            self.status = status
        if subnet is not None:
            self.subnet = subnet
        if subnet_mask is not None:
            self.subnet_mask = subnet_mask

    @property
    def gateway(self):
        """Gets the gateway of this InlineResponse200.  # noqa: E501

        The gateway for this subnet  # noqa: E501

        :return: The gateway of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this InlineResponse200.

        The gateway for this subnet  # noqa: E501

        :param gateway: The gateway of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def ip_addr(self):
        """Gets the ip_addr of this InlineResponse200.  # noqa: E501

        the ip address...  # noqa: E501

        :return: The ip_addr of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this InlineResponse200.

        the ip address...  # noqa: E501

        :param ip_addr: The ip_addr of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._ip_addr = ip_addr

    @property
    def status(self):
        """Gets the status of this InlineResponse200.  # noqa: E501

        status of this ip addrs  # noqa: E501

        :return: The status of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200.

        status of this ip addrs  # noqa: E501

        :param status: The status of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet(self):
        """Gets the subnet of this InlineResponse200.  # noqa: E501

        subnet this ip addres belongs to  # noqa: E501

        :return: The subnet of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this InlineResponse200.

        subnet this ip addres belongs to  # noqa: E501

        :param subnet: The subnet of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._subnet = subnet

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this InlineResponse200.  # noqa: E501

        The subnetmask for this subnet  # noqa: E501

        :return: The subnet_mask of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this InlineResponse200.

        The subnetmask for this subnet  # noqa: E501

        :param subnet_mask: The subnet_mask of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._subnet_mask = subnet_mask

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
