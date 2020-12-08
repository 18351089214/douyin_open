# coding: utf-8

"""

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
        'merchant_id': 'int',
        'live_id': 'int',
        'biz_order_no': 'str',
        'trans_code': 'str',
        'order_name': 'str',
        'order_desc': 'str',
        'amount': 'int',
        'remark': 'str'
    }

    attribute_map = {
        'merchant_id': 'merchant_id',
        'live_id': 'live_id',
        'biz_order_no': 'biz_order_no',
        'trans_code': 'trans_code',
        'order_name': 'order_name',
        'order_desc': 'order_desc',
        'amount': 'amount',
        'remark': 'remark'
    }

    def __init__(self, merchant_id=None, live_id=None, biz_order_no=None, trans_code=None, order_name=None, order_desc=None, amount=None, remark=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501
        self._merchant_id = None
        self._live_id = None
        self._biz_order_no = None
        self._trans_code = None
        self._order_name = None
        self._order_desc = None
        self._amount = None
        self._remark = None
        self.discriminator = None
        self.merchant_id = merchant_id
        self.live_id = live_id
        self.biz_order_no = biz_order_no
        self.trans_code = trans_code
        self.order_name = order_name
        self.order_desc = order_desc
        self.amount = amount
        self.remark = remark

    @property
    def merchant_id(self):
        """Gets the merchant_id of this Body.  # noqa: E501

        商户id  # noqa: E501

        :return: The merchant_id of this Body.  # noqa: E501
        :rtype: int
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this Body.

        商户id  # noqa: E501

        :param merchant_id: The merchant_id of this Body.  # noqa: E501
        :type: int
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def live_id(self):
        """Gets the live_id of this Body.  # noqa: E501

        业务id  # noqa: E501

        :return: The live_id of this Body.  # noqa: E501
        :rtype: int
        """
        return self._live_id

    @live_id.setter
    def live_id(self, live_id):
        """Sets the live_id of this Body.

        业务id  # noqa: E501

        :param live_id: The live_id of this Body.  # noqa: E501
        :type: int
        """
        if live_id is None:
            raise ValueError("Invalid value for `live_id`, must not be `None`")  # noqa: E501

        self._live_id = live_id

    @property
    def biz_order_no(self):
        """Gets the biz_order_no of this Body.  # noqa: E501

        外部订单号，由调用方生成，长度小于64  # noqa: E501

        :return: The biz_order_no of this Body.  # noqa: E501
        :rtype: str
        """
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, biz_order_no):
        """Sets the biz_order_no of this Body.

        外部订单号，由调用方生成，长度小于64  # noqa: E501

        :param biz_order_no: The biz_order_no of this Body.  # noqa: E501
        :type: str
        """
        if biz_order_no is None:
            raise ValueError("Invalid value for `biz_order_no`, must not be `None`")  # noqa: E501

        self._biz_order_no = biz_order_no

    @property
    def trans_code(self):
        """Gets the trans_code of this Body.  # noqa: E501

        交易场景码，SEND_MONEY_REDPACKET: 红包转账 SEND_VCOIN_REDPACKET: 抖币转账  # noqa: E501

        :return: The trans_code of this Body.  # noqa: E501
        :rtype: str
        """
        return self._trans_code

    @trans_code.setter
    def trans_code(self, trans_code):
        """Sets the trans_code of this Body.

        交易场景码，SEND_MONEY_REDPACKET: 红包转账 SEND_VCOIN_REDPACKET: 抖币转账  # noqa: E501

        :param trans_code: The trans_code of this Body.  # noqa: E501
        :type: str
        """
        if trans_code is None:
            raise ValueError("Invalid value for `trans_code`, must not be `None`")  # noqa: E501

        self._trans_code = trans_code

    @property
    def order_name(self):
        """Gets the order_name of this Body.  # noqa: E501

        订单名称，长度小于64  # noqa: E501

        :return: The order_name of this Body.  # noqa: E501
        :rtype: str
        """
        return self._order_name

    @order_name.setter
    def order_name(self, order_name):
        """Sets the order_name of this Body.

        订单名称，长度小于64  # noqa: E501

        :param order_name: The order_name of this Body.  # noqa: E501
        :type: str
        """
        if order_name is None:
            raise ValueError("Invalid value for `order_name`, must not be `None`")  # noqa: E501

        self._order_name = order_name

    @property
    def order_desc(self):
        """Gets the order_desc of this Body.  # noqa: E501

        订单描述，长度小于256  # noqa: E501

        :return: The order_desc of this Body.  # noqa: E501
        :rtype: str
        """
        return self._order_desc

    @order_desc.setter
    def order_desc(self, order_desc):
        """Sets the order_desc of this Body.

        订单描述，长度小于256  # noqa: E501

        :param order_desc: The order_desc of this Body.  # noqa: E501
        :type: str
        """
        if order_desc is None:
            raise ValueError("Invalid value for `order_desc`, must not be `None`")  # noqa: E501

        self._order_desc = order_desc

    @property
    def amount(self):
        """Gets the amount of this Body.  # noqa: E501

        数目  # noqa: E501

        :return: The amount of this Body.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Body.

        数目  # noqa: E501

        :param amount: The amount of this Body.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def remark(self):
        """Gets the remark of this Body.  # noqa: E501

        标记，长度小于512  # noqa: E501

        :return: The remark of this Body.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this Body.

        标记，长度小于512  # noqa: E501

        :param remark: The remark of this Body.  # noqa: E501
        :type: str
        """
        if remark is None:
            raise ValueError("Invalid value for `remark`, must not be `None`")  # noqa: E501

        self._remark = remark

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
