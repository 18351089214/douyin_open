# coding: utf-8

"""

    仅对内提供  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse200DataList(object):
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
        'title': 'str',
        'cover': 'ImgUrl',
        'author': 'str',
        'duration': 'int',
        'id': 'int',
        'isrc': 'str',
        'meta_song_id': 'str'
    }

    attribute_map = {
        'title': 'title',
        'cover': 'cover',
        'author': 'author',
        'duration': 'duration',
        'id': 'id',
        'isrc': 'isrc',
        'meta_song_id': 'meta_song_id'
    }

    def __init__(self, title=None, cover=None, author=None, duration=None, id=None, isrc=None, meta_song_id=None):  # noqa: E501
        """InlineResponse200DataList - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._cover = None
        self._author = None
        self._duration = None
        self._id = None
        self._isrc = None
        self._meta_song_id = None
        self.discriminator = None
        self.title = title
        if cover is not None:
            self.cover = cover
        self.author = author
        self.duration = duration
        self.id = id
        if isrc is not None:
            self.isrc = isrc
        if meta_song_id is not None:
            self.meta_song_id = meta_song_id

    @property
    def title(self):
        """Gets the title of this InlineResponse200DataList.  # noqa: E501

        音乐标题  # noqa: E501

        :return: The title of this InlineResponse200DataList.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineResponse200DataList.

        音乐标题  # noqa: E501

        :param title: The title of this InlineResponse200DataList.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def cover(self):
        """Gets the cover of this InlineResponse200DataList.  # noqa: E501


        :return: The cover of this InlineResponse200DataList.  # noqa: E501
        :rtype: ImgUrl
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """Sets the cover of this InlineResponse200DataList.


        :param cover: The cover of this InlineResponse200DataList.  # noqa: E501
        :type: ImgUrl
        """

        self._cover = cover

    @property
    def author(self):
        """Gets the author of this InlineResponse200DataList.  # noqa: E501

        作者  # noqa: E501

        :return: The author of this InlineResponse200DataList.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this InlineResponse200DataList.

        作者  # noqa: E501

        :param author: The author of this InlineResponse200DataList.  # noqa: E501
        :type: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def duration(self):
        """Gets the duration of this InlineResponse200DataList.  # noqa: E501

        时长  # noqa: E501

        :return: The duration of this InlineResponse200DataList.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse200DataList.

        时长  # noqa: E501

        :param duration: The duration of this InlineResponse200DataList.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def id(self):
        """Gets the id of this InlineResponse200DataList.  # noqa: E501


        :return: The id of this InlineResponse200DataList.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200DataList.


        :param id: The id of this InlineResponse200DataList.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def isrc(self):
        """Gets the isrc of this InlineResponse200DataList.  # noqa: E501

        音乐isrc  # noqa: E501

        :return: The isrc of this InlineResponse200DataList.  # noqa: E501
        :rtype: str
        """
        return self._isrc

    @isrc.setter
    def isrc(self, isrc):
        """Sets the isrc of this InlineResponse200DataList.

        音乐isrc  # noqa: E501

        :param isrc: The isrc of this InlineResponse200DataList.  # noqa: E501
        :type: str
        """

        self._isrc = isrc

    @property
    def meta_song_id(self):
        """Gets the meta_song_id of this InlineResponse200DataList.  # noqa: E501

        音乐MetaSongID  # noqa: E501

        :return: The meta_song_id of this InlineResponse200DataList.  # noqa: E501
        :rtype: str
        """
        return self._meta_song_id

    @meta_song_id.setter
    def meta_song_id(self, meta_song_id):
        """Sets the meta_song_id of this InlineResponse200DataList.

        音乐MetaSongID  # noqa: E501

        :param meta_song_id: The meta_song_id of this InlineResponse200DataList.  # noqa: E501
        :type: str
        """

        self._meta_song_id = meta_song_id

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
        if issubclass(InlineResponse200DataList, dict):
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
        if not isinstance(other, InlineResponse200DataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
