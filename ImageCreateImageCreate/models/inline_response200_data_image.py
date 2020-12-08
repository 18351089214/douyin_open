# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse200DataImage(object):
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
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'image_id': 'image_id',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, image_id=None, width=None, height=None):  # noqa: E501
        """InlineResponse200DataImage - a model defined in Swagger"""  # noqa: E501
        self._image_id = None
        self._width = None
        self._height = None
        self.discriminator = None
        self.image_id = image_id
        self.width = width
        self.height = height

    @property
    def image_id(self):
        """Gets the image_id of this InlineResponse200DataImage.  # noqa: E501

        图片id  # noqa: E501

        :return: The image_id of this InlineResponse200DataImage.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this InlineResponse200DataImage.

        图片id  # noqa: E501

        :param image_id: The image_id of this InlineResponse200DataImage.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def width(self):
        """Gets the width of this InlineResponse200DataImage.  # noqa: E501


        :return: The width of this InlineResponse200DataImage.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this InlineResponse200DataImage.


        :param width: The width of this InlineResponse200DataImage.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this InlineResponse200DataImage.  # noqa: E501


        :return: The height of this InlineResponse200DataImage.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this InlineResponse200DataImage.


        :param height: The height of this InlineResponse200DataImage.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

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
        if issubclass(InlineResponse200DataImage, dict):
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
        if not isinstance(other, InlineResponse200DataImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
