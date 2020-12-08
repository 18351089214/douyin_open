# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body1(object):
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
        'image_id': 'str',
        'text': 'str',
        'poi_id': 'str',
        'poi_name': 'str',
        'micro_app_id': 'str',
        'micro_app_title': 'str',
        'micro_app_url': 'str',
        'at_users': 'list[str]'
    }

    attribute_map = {
        'image_id': 'image_id',
        'text': 'text',
        'poi_id': 'poi_id',
        'poi_name': 'poi_name',
        'micro_app_id': 'micro_app_id',
        'micro_app_title': 'micro_app_title',
        'micro_app_url': 'micro_app_url',
        'at_users': 'at_users'
    }

    def __init__(self, image_id=None, text=None, poi_id=None, poi_name=None, micro_app_id=None, micro_app_title=None, micro_app_url=None, at_users=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501
        self._image_id = None
        self._text = None
        self._poi_id = None
        self._poi_name = None
        self._micro_app_id = None
        self._micro_app_title = None
        self._micro_app_url = None
        self._at_users = None
        self.discriminator = None
        self.image_id = image_id
        if text is not None:
            self.text = text
        if poi_id is not None:
            self.poi_id = poi_id
        if poi_name is not None:
            self.poi_name = poi_name
        if micro_app_id is not None:
            self.micro_app_id = micro_app_id
        if micro_app_title is not None:
            self.micro_app_title = micro_app_title
        if micro_app_url is not None:
            self.micro_app_url = micro_app_url
        if at_users is not None:
            self.at_users = at_users

    @property
    def image_id(self):
        """Gets the image_id of this Body1.  # noqa: E501

        通过/image/upload/接口得到。  # noqa: E501

        :return: The image_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Body1.

        通过/image/upload/接口得到。  # noqa: E501

        :param image_id: The image_id of this Body1.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def text(self):
        """Gets the text of this Body1.  # noqa: E501

        标题，可以带话题。 如title1#话题1 #话题2 注意：话题审核依旧遵循抖音的审核逻辑，强烈建议第三方谨慎拟定话题名称，避免强导流行为。   # noqa: E501

        :return: The text of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Body1.

        标题，可以带话题。 如title1#话题1 #话题2 注意：话题审核依旧遵循抖音的审核逻辑，强烈建议第三方谨慎拟定话题名称，避免强导流行为。   # noqa: E501

        :param text: The text of this Body1.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def poi_id(self):
        """Gets the poi_id of this Body1.  # noqa: E501

        地理位置id  # noqa: E501

        :return: The poi_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._poi_id

    @poi_id.setter
    def poi_id(self, poi_id):
        """Sets the poi_id of this Body1.

        地理位置id  # noqa: E501

        :param poi_id: The poi_id of this Body1.  # noqa: E501
        :type: str
        """

        self._poi_id = poi_id

    @property
    def poi_name(self):
        """Gets the poi_name of this Body1.  # noqa: E501

        地理位置名称  # noqa: E501

        :return: The poi_name of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._poi_name

    @poi_name.setter
    def poi_name(self, poi_name):
        """Sets the poi_name of this Body1.

        地理位置名称  # noqa: E501

        :param poi_name: The poi_name of this Body1.  # noqa: E501
        :type: str
        """

        self._poi_name = poi_name

    @property
    def micro_app_id(self):
        """Gets the micro_app_id of this Body1.  # noqa: E501

        小程序id  # noqa: E501

        :return: The micro_app_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._micro_app_id

    @micro_app_id.setter
    def micro_app_id(self, micro_app_id):
        """Sets the micro_app_id of this Body1.

        小程序id  # noqa: E501

        :param micro_app_id: The micro_app_id of this Body1.  # noqa: E501
        :type: str
        """

        self._micro_app_id = micro_app_id

    @property
    def micro_app_title(self):
        """Gets the micro_app_title of this Body1.  # noqa: E501

        小程序标题  # noqa: E501

        :return: The micro_app_title of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._micro_app_title

    @micro_app_title.setter
    def micro_app_title(self, micro_app_title):
        """Sets the micro_app_title of this Body1.

        小程序标题  # noqa: E501

        :param micro_app_title: The micro_app_title of this Body1.  # noqa: E501
        :type: str
        """

        self._micro_app_title = micro_app_title

    @property
    def micro_app_url(self):
        """Gets the micro_app_url of this Body1.  # noqa: E501

        吊起小程序时的参数  # noqa: E501

        :return: The micro_app_url of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._micro_app_url

    @micro_app_url.setter
    def micro_app_url(self, micro_app_url):
        """Sets the micro_app_url of this Body1.

        吊起小程序时的参数  # noqa: E501

        :param micro_app_url: The micro_app_url of this Body1.  # noqa: E501
        :type: str
        """

        self._micro_app_url = micro_app_url

    @property
    def at_users(self):
        """Gets the at_users of this Body1.  # noqa: E501

        如果需要at其他用户。将text中@nickname对应的open_id放到这里。  # noqa: E501

        :return: The at_users of this Body1.  # noqa: E501
        :rtype: list[str]
        """
        return self._at_users

    @at_users.setter
    def at_users(self, at_users):
        """Sets the at_users of this Body1.

        如果需要at其他用户。将text中@nickname对应的open_id放到这里。  # noqa: E501

        :param at_users: The at_users of this Body1.  # noqa: E501
        :type: list[str]
        """

        self._at_users = at_users

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
