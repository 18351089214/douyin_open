# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse2001Data(object):
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
        'access_token': 'str',
        'expires_in': 'str',
        'refresh_token': 'str',
        'open_id': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'description': 'description',
        'access_token': 'access_token',
        'expires_in': 'expires_in',
        'refresh_token': 'refresh_token',
        'open_id': 'open_id',
        'scope': 'scope'
    }

    def __init__(self, error_code=None, description=None, access_token=None, expires_in=None, refresh_token=None, open_id=None, scope=None):  # noqa: E501
        """InlineResponse2001Data - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._description = None
        self._access_token = None
        self._expires_in = None
        self._refresh_token = None
        self._open_id = None
        self._scope = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if description is not None:
            self.description = description
        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if open_id is not None:
            self.open_id = open_id
        if scope is not None:
            self.scope = scope

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse2001Data.  # noqa: E501


        :return: The error_code of this InlineResponse2001Data.  # noqa: E501
        :rtype: ErrorCode
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse2001Data.


        :param error_code: The error_code of this InlineResponse2001Data.  # noqa: E501
        :type: ErrorCode
        """

        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this InlineResponse2001Data.  # noqa: E501


        :return: The description of this InlineResponse2001Data.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse2001Data.


        :param description: The description of this InlineResponse2001Data.  # noqa: E501
        :type: Description
        """

        self._description = description

    @property
    def access_token(self):
        """Gets the access_token of this InlineResponse2001Data.  # noqa: E501

        接口调用凭证  # noqa: E501

        :return: The access_token of this InlineResponse2001Data.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this InlineResponse2001Data.

        接口调用凭证  # noqa: E501

        :param access_token: The access_token of this InlineResponse2001Data.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this InlineResponse2001Data.  # noqa: E501

        过期时间，单位（秒）  # noqa: E501

        :return: The expires_in of this InlineResponse2001Data.  # noqa: E501
        :rtype: str
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this InlineResponse2001Data.

        过期时间，单位（秒）  # noqa: E501

        :param expires_in: The expires_in of this InlineResponse2001Data.  # noqa: E501
        :type: str
        """

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """Gets the refresh_token of this InlineResponse2001Data.  # noqa: E501

        用户刷新  # noqa: E501

        :return: The refresh_token of this InlineResponse2001Data.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this InlineResponse2001Data.

        用户刷新  # noqa: E501

        :param refresh_token: The refresh_token of this InlineResponse2001Data.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def open_id(self):
        """Gets the open_id of this InlineResponse2001Data.  # noqa: E501

        当前应用下，授权用户唯一标识  # noqa: E501

        :return: The open_id of this InlineResponse2001Data.  # noqa: E501
        :rtype: str
        """
        return self._open_id

    @open_id.setter
    def open_id(self, open_id):
        """Sets the open_id of this InlineResponse2001Data.

        当前应用下，授权用户唯一标识  # noqa: E501

        :param open_id: The open_id of this InlineResponse2001Data.  # noqa: E501
        :type: str
        """

        self._open_id = open_id

    @property
    def scope(self):
        """Gets the scope of this InlineResponse2001Data.  # noqa: E501

        用户授权的作用域  # noqa: E501

        :return: The scope of this InlineResponse2001Data.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this InlineResponse2001Data.

        用户授权的作用域  # noqa: E501

        :param scope: The scope of this InlineResponse2001Data.  # noqa: E501
        :type: str
        """

        self._scope = scope

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
        if issubclass(InlineResponse2001Data, dict):
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
        if not isinstance(other, InlineResponse2001Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
