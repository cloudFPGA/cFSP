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

class Instance(object):
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
        'fpga_board': 'str',
        'image_id': 'str',
        'instance_id': 'int',
        'project_name': 'str',
        'role_ip': 'str',
        'shell_type': 'str',
        'slot_num': 'int',
        'status': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'fpga_board': 'fpga_board',
        'image_id': 'image_id',
        'instance_id': 'instance_id',
        'project_name': 'project_name',
        'role_ip': 'role_ip',
        'shell_type': 'shell_type',
        'slot_num': 'slot_num',
        'status': 'status',
        'user_id': 'user_id'
    }

    def __init__(self, fpga_board=None, image_id=None, instance_id=None, project_name=None, role_ip=None, shell_type=None, slot_num=None, status=None, user_id=None):  # noqa: E501
        """Instance - a model defined in Swagger"""  # noqa: E501
        self._fpga_board = None
        self._image_id = None
        self._instance_id = None
        self._project_name = None
        self._role_ip = None
        self._shell_type = None
        self._slot_num = None
        self._status = None
        self._user_id = None
        self.discriminator = None
        if fpga_board is not None:
            self.fpga_board = fpga_board
        if image_id is not None:
            self.image_id = image_id
        if instance_id is not None:
            self.instance_id = instance_id
        if project_name is not None:
            self.project_name = project_name
        if role_ip is not None:
            self.role_ip = role_ip
        if shell_type is not None:
            self.shell_type = shell_type
        if slot_num is not None:
            self.slot_num = slot_num
        if status is not None:
            self.status = status
        if user_id is not None:
            self.user_id = user_id

    @property
    def fpga_board(self):
        """Gets the fpga_board of this Instance.  # noqa: E501

        Type of cloudFPGA  # noqa: E501

        :return: The fpga_board of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._fpga_board

    @fpga_board.setter
    def fpga_board(self, fpga_board):
        """Sets the fpga_board of this Instance.

        Type of cloudFPGA  # noqa: E501

        :param fpga_board: The fpga_board of this Instance.  # noqa: E501
        :type: str
        """

        self._fpga_board = fpga_board

    @property
    def image_id(self):
        """Gets the image_id of this Instance.  # noqa: E501

        Image ID  # noqa: E501

        :return: The image_id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Instance.

        Image ID  # noqa: E501

        :param image_id: The image_id of this Instance.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_id(self):
        """Gets the instance_id of this Instance.  # noqa: E501

        ID of the instance  # noqa: E501

        :return: The instance_id of this Instance.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Instance.

        ID of the instance  # noqa: E501

        :param instance_id: The instance_id of this Instance.  # noqa: E501
        :type: int
        """

        self._instance_id = instance_id

    @property
    def project_name(self):
        """Gets the project_name of this Instance.  # noqa: E501

        Name of the OpenStack project the quota should be acounted to, if a user has multiple projects.  # noqa: E501

        :return: The project_name of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this Instance.

        Name of the OpenStack project the quota should be acounted to, if a user has multiple projects.  # noqa: E501

        :param project_name: The project_name of this Instance.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def role_ip(self):
        """Gets the role_ip of this Instance.  # noqa: E501

        IP of sled manager  # noqa: E501

        :return: The role_ip of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._role_ip

    @role_ip.setter
    def role_ip(self, role_ip):
        """Sets the role_ip of this Instance.

        IP of sled manager  # noqa: E501

        :param role_ip: The role_ip of this Instance.  # noqa: E501
        :type: str
        """

        self._role_ip = role_ip

    @property
    def shell_type(self):
        """Gets the shell_type of this Instance.  # noqa: E501

        Type of the current Shell (interface) of the FPGA  # noqa: E501

        :return: The shell_type of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._shell_type

    @shell_type.setter
    def shell_type(self, shell_type):
        """Sets the shell_type of this Instance.

        Type of the current Shell (interface) of the FPGA  # noqa: E501

        :param shell_type: The shell_type of this Instance.  # noqa: E501
        :type: str
        """

        self._shell_type = shell_type

    @property
    def slot_num(self):
        """Gets the slot_num of this Instance.  # noqa: E501

        Slot number of resource  # noqa: E501

        :return: The slot_num of this Instance.  # noqa: E501
        :rtype: int
        """
        return self._slot_num

    @slot_num.setter
    def slot_num(self, slot_num):
        """Sets the slot_num of this Instance.

        Slot number of resource  # noqa: E501

        :param slot_num: The slot_num of this Instance.  # noqa: E501
        :type: int
        """

        self._slot_num = slot_num

    @property
    def status(self):
        """Gets the status of this Instance.  # noqa: E501

        Status of instance  # noqa: E501

        :return: The status of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Instance.

        Status of instance  # noqa: E501

        :param status: The status of this Instance.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_id(self):
        """Gets the user_id of this Instance.  # noqa: E501

        User ID  # noqa: E501

        :return: The user_id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Instance.

        User ID  # noqa: E501

        :param user_id: The user_id of this Instance.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(Instance, dict):
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
        if not isinstance(other, Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
