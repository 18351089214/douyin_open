# coding: utf-8

"""
    查看券码状态

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CodeInfo(object):
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
        'groupon_id': 'str',
        'code': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'confirm_time': 'int',
        'status': 'int'
    }

    attribute_map = {
        'groupon_id': 'groupon_id',
        'code': 'code',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'confirm_time': 'confirm_time',
        'status': 'status'
    }

    def __init__(self, groupon_id=None, code=None, start_time=None, end_time=None, confirm_time=None, status=None):  # noqa: E501
        """CodeInfo - a model defined in Swagger"""  # noqa: E501
        self._groupon_id = None
        self._code = None
        self._start_time = None
        self._end_time = None
        self._confirm_time = None
        self._status = None
        self.discriminator = None
        if groupon_id is not None:
            self.groupon_id = groupon_id
        if code is not None:
            self.code = code
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if confirm_time is not None:
            self.confirm_time = confirm_time
        if status is not None:
            self.status = status

    @property
    def groupon_id(self):
        """Gets the groupon_id of this CodeInfo.  # noqa: E501

        团购活动的ID  # noqa: E501

        :return: The groupon_id of this CodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._groupon_id

    @groupon_id.setter
    def groupon_id(self, groupon_id):
        """Sets the groupon_id of this CodeInfo.

        团购活动的ID  # noqa: E501

        :param groupon_id: The groupon_id of this CodeInfo.  # noqa: E501
        :type: str
        """

        self._groupon_id = groupon_id

    @property
    def code(self):
        """Gets the code of this CodeInfo.  # noqa: E501

        劵码值  # noqa: E501

        :return: The code of this CodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CodeInfo.

        劵码值  # noqa: E501

        :param code: The code of this CodeInfo.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def start_time(self):
        """Gets the start_time of this CodeInfo.  # noqa: E501

        劵码有效的起始时间  # noqa: E501

        :return: The start_time of this CodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CodeInfo.

        劵码有效的起始时间  # noqa: E501

        :param start_time: The start_time of this CodeInfo.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CodeInfo.  # noqa: E501

        劵码有效的终止时间  # noqa: E501

        :return: The end_time of this CodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CodeInfo.

        劵码有效的终止时间  # noqa: E501

        :param end_time: The end_time of this CodeInfo.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def confirm_time(self):
        """Gets the confirm_time of this CodeInfo.  # noqa: E501

        核销时间  # noqa: E501

        :return: The confirm_time of this CodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, confirm_time):
        """Sets the confirm_time of this CodeInfo.

        核销时间  # noqa: E501

        :param confirm_time: The confirm_time of this CodeInfo.  # noqa: E501
        :type: int
        """

        self._confirm_time = confirm_time

    @property
    def status(self):
        """Gets the status of this CodeInfo.  # noqa: E501

        * 劵码的状态   * -1: 不存在   * 1: 未核销   * 2: 已核销   # noqa: E501

        :return: The status of this CodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CodeInfo.

        * 劵码的状态   * -1: 不存在   * 1: 未核销   * 2: 已核销   # noqa: E501

        :param status: The status of this CodeInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [-1, 1, 2, ""]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(CodeInfo, dict):
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
        if not isinstance(other, CodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
