# coding: utf-8

"""
    团购活动详情

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse200Data(object):
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
        'error_code': 'ErrorCode',
        'description': 'Description',
        'groupons': 'list[GrouponItem]'
    }

    attribute_map = {
        'error_code': 'error_code',
        'description': 'description',
        'groupons': 'groupons'
    }

    def __init__(self, error_code=None, description=None, groupons=None):  # noqa: E501
        """InlineResponse200Data - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._description = None
        self._groupons = None
        self.discriminator = None
        self.error_code = error_code
        self.description = description
        if groupons is not None:
            self.groupons = groupons

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse200Data.  # noqa: E501


        :return: The error_code of this InlineResponse200Data.  # noqa: E501
        :rtype: ErrorCode
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse200Data.


        :param error_code: The error_code of this InlineResponse200Data.  # noqa: E501
        :type: ErrorCode
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this InlineResponse200Data.  # noqa: E501


        :return: The description of this InlineResponse200Data.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse200Data.


        :param description: The description of this InlineResponse200Data.  # noqa: E501
        :type: Description
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def groupons(self):
        """Gets the groupons of this InlineResponse200Data.  # noqa: E501


        :return: The groupons of this InlineResponse200Data.  # noqa: E501
        :rtype: list[GrouponItem]
        """
        return self._groupons

    @groupons.setter
    def groupons(self, groupons):
        """Sets the groupons of this InlineResponse200Data.


        :param groupons: The groupons of this InlineResponse200Data.  # noqa: E501
        :type: list[GrouponItem]
        """

        self._groupons = groupons

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
        if issubclass(InlineResponse200Data, dict):
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
        if not isinstance(other, InlineResponse200Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
