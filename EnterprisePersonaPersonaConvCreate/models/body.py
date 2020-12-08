# coding: utf-8

"""
    客服会话创建

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body(object):
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
        'to_user_id': 'str',
        'persona_id': 'str'
    }

    attribute_map = {
        'to_user_id': 'to_user_id',
        'persona_id': 'persona_id'
    }

    def __init__(self, to_user_id=None, persona_id=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501
        self._to_user_id = None
        self._persona_id = None
        self.discriminator = None
        self.to_user_id = to_user_id
        self.persona_id = persona_id

    @property
    def to_user_id(self):
        """Gets the to_user_id of this Body.  # noqa: E501

        会话对方的open_id  # noqa: E501

        :return: The to_user_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, to_user_id):
        """Sets the to_user_id of this Body.

        会话对方的open_id  # noqa: E501

        :param to_user_id: The to_user_id of this Body.  # noqa: E501
        :type: str
        """
        if to_user_id is None:
            raise ValueError("Invalid value for `to_user_id`, must not be `None`")  # noqa: E501

        self._to_user_id = to_user_id

    @property
    def persona_id(self):
        """Gets the persona_id of this Body.  # noqa: E501

        客服id  # noqa: E501

        :return: The persona_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._persona_id

    @persona_id.setter
    def persona_id(self, persona_id):
        """Sets the persona_id of this Body.

        客服id  # noqa: E501

        :param persona_id: The persona_id of this Body.  # noqa: E501
        :type: str
        """
        if persona_id is None:
            raise ValueError("Invalid value for `persona_id`, must not be `None`")  # noqa: E501

        self._persona_id = persona_id

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
