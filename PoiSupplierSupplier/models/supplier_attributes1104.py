# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SupplierAttributes1104(object):
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
        'check_in_time': 'str',
        'check_out_time': 'str',
        'breakfast': 'SupplierAttributes1104Breakfast',
        'child': 'str',
        'pet': 'str'
    }

    attribute_map = {
        'check_in_time': 'check_in_time',
        'check_out_time': 'check_out_time',
        'breakfast': 'breakfast',
        'child': 'child',
        'pet': 'pet'
    }

    def __init__(self, check_in_time=None, check_out_time=None, breakfast=None, child=None, pet=None):  # noqa: E501
        """SupplierAttributes1104 - a model defined in Swagger"""  # noqa: E501
        self._check_in_time = None
        self._check_out_time = None
        self._breakfast = None
        self._child = None
        self._pet = None
        self.discriminator = None
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.breakfast = breakfast
        if child is not None:
            self.child = child
        if pet is not None:
            self.pet = pet

    @property
    def check_in_time(self):
        """Gets the check_in_time of this SupplierAttributes1104.  # noqa: E501

        入住时间(HH:mm)  # noqa: E501

        :return: The check_in_time of this SupplierAttributes1104.  # noqa: E501
        :rtype: str
        """
        return self._check_in_time

    @check_in_time.setter
    def check_in_time(self, check_in_time):
        """Sets the check_in_time of this SupplierAttributes1104.

        入住时间(HH:mm)  # noqa: E501

        :param check_in_time: The check_in_time of this SupplierAttributes1104.  # noqa: E501
        :type: str
        """
        if check_in_time is None:
            raise ValueError("Invalid value for `check_in_time`, must not be `None`")  # noqa: E501

        self._check_in_time = check_in_time

    @property
    def check_out_time(self):
        """Gets the check_out_time of this SupplierAttributes1104.  # noqa: E501

        离店时间(HH:mm)  # noqa: E501

        :return: The check_out_time of this SupplierAttributes1104.  # noqa: E501
        :rtype: str
        """
        return self._check_out_time

    @check_out_time.setter
    def check_out_time(self, check_out_time):
        """Sets the check_out_time of this SupplierAttributes1104.

        离店时间(HH:mm)  # noqa: E501

        :param check_out_time: The check_out_time of this SupplierAttributes1104.  # noqa: E501
        :type: str
        """
        if check_out_time is None:
            raise ValueError("Invalid value for `check_out_time`, must not be `None`")  # noqa: E501

        self._check_out_time = check_out_time

    @property
    def breakfast(self):
        """Gets the breakfast of this SupplierAttributes1104.  # noqa: E501


        :return: The breakfast of this SupplierAttributes1104.  # noqa: E501
        :rtype: SupplierAttributes1104Breakfast
        """
        return self._breakfast

    @breakfast.setter
    def breakfast(self, breakfast):
        """Sets the breakfast of this SupplierAttributes1104.


        :param breakfast: The breakfast of this SupplierAttributes1104.  # noqa: E501
        :type: SupplierAttributes1104Breakfast
        """
        if breakfast is None:
            raise ValueError("Invalid value for `breakfast`, must not be `None`")  # noqa: E501

        self._breakfast = breakfast

    @property
    def child(self):
        """Gets the child of this SupplierAttributes1104.  # noqa: E501

        儿童政策(<=500字)  # noqa: E501

        :return: The child of this SupplierAttributes1104.  # noqa: E501
        :rtype: str
        """
        return self._child

    @child.setter
    def child(self, child):
        """Sets the child of this SupplierAttributes1104.

        儿童政策(<=500字)  # noqa: E501

        :param child: The child of this SupplierAttributes1104.  # noqa: E501
        :type: str
        """

        self._child = child

    @property
    def pet(self):
        """Gets the pet of this SupplierAttributes1104.  # noqa: E501

        宠物政策(<=500字)  # noqa: E501

        :return: The pet of this SupplierAttributes1104.  # noqa: E501
        :rtype: str
        """
        return self._pet

    @pet.setter
    def pet(self, pet):
        """Sets the pet of this SupplierAttributes1104.

        宠物政策(<=500字)  # noqa: E501

        :param pet: The pet of this SupplierAttributes1104.  # noqa: E501
        :type: str
        """

        self._pet = pet

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
        if issubclass(SupplierAttributes1104, dict):
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
        if not isinstance(other, SupplierAttributes1104):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
