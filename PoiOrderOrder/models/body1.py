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
        'order_id': 'str',
        'spu_ext_id': 'str',
        'status': 'int',
        'reserve_amount': 'int',
        'customer_name': 'str',
        'customer_phone': 'str',
        'customer_list': 'list[PoiexthotelordercommitCustomerList]',
        'check_in': 'str',
        'check_out': 'str',
        'total_price': 'int',
        'remark': 'str',
        'date_price': 'list[PoiexthotelordercommitDatePrice]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'spu_ext_id': 'spu_ext_id',
        'status': 'status',
        'reserve_amount': 'reserve_amount',
        'customer_name': 'customer_name',
        'customer_phone': 'customer_phone',
        'customer_list': 'customer_list',
        'check_in': 'check_in',
        'check_out': 'check_out',
        'total_price': 'total_price',
        'remark': 'remark',
        'date_price': 'date_price'
    }

    def __init__(self, order_id=None, spu_ext_id=None, status=None, reserve_amount=None, customer_name=None, customer_phone=None, customer_list=None, check_in=None, check_out=None, total_price=None, remark=None, date_price=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._spu_ext_id = None
        self._status = None
        self._reserve_amount = None
        self._customer_name = None
        self._customer_phone = None
        self._customer_list = None
        self._check_in = None
        self._check_out = None
        self._total_price = None
        self._remark = None
        self._date_price = None
        self.discriminator = None
        self.order_id = order_id
        self.spu_ext_id = spu_ext_id
        self.status = status
        self.reserve_amount = reserve_amount
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        if customer_list is not None:
            self.customer_list = customer_list
        self.check_in = check_in
        self.check_out = check_out
        self.total_price = total_price
        if remark is not None:
            self.remark = remark
        if date_price is not None:
            self.date_price = date_price

    @property
    def order_id(self):
        """Gets the order_id of this Body1.  # noqa: E501

        抖音订单号  # noqa: E501

        :return: The order_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Body1.

        抖音订单号  # noqa: E501

        :param order_id: The order_id of this Body1.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def spu_ext_id(self):
        """Gets the spu_ext_id of this Body1.  # noqa: E501

        接入方房型ID  # noqa: E501

        :return: The spu_ext_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._spu_ext_id

    @spu_ext_id.setter
    def spu_ext_id(self, spu_ext_id):
        """Sets the spu_ext_id of this Body1.

        接入方房型ID  # noqa: E501

        :param spu_ext_id: The spu_ext_id of this Body1.  # noqa: E501
        :type: str
        """
        if spu_ext_id is None:
            raise ValueError("Invalid value for `spu_ext_id`, must not be `None`")  # noqa: E501

        self._spu_ext_id = spu_ext_id

    @property
    def status(self):
        """Gets the status of this Body1.  # noqa: E501

        订单支付状态。0 - 未支付, 1 - 已支付  # noqa: E501

        :return: The status of this Body1.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Body1.

        订单支付状态。0 - 未支付, 1 - 已支付  # noqa: E501

        :param status: The status of this Body1.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def reserve_amount(self):
        """Gets the reserve_amount of this Body1.  # noqa: E501

        预定数量  # noqa: E501

        :return: The reserve_amount of this Body1.  # noqa: E501
        :rtype: int
        """
        return self._reserve_amount

    @reserve_amount.setter
    def reserve_amount(self, reserve_amount):
        """Sets the reserve_amount of this Body1.

        预定数量  # noqa: E501

        :param reserve_amount: The reserve_amount of this Body1.  # noqa: E501
        :type: int
        """
        if reserve_amount is None:
            raise ValueError("Invalid value for `reserve_amount`, must not be `None`")  # noqa: E501

        self._reserve_amount = reserve_amount

    @property
    def customer_name(self):
        """Gets the customer_name of this Body1.  # noqa: E501

        预订人姓名  # noqa: E501

        :return: The customer_name of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this Body1.

        预订人姓名  # noqa: E501

        :param customer_name: The customer_name of this Body1.  # noqa: E501
        :type: str
        """
        if customer_name is None:
            raise ValueError("Invalid value for `customer_name`, must not be `None`")  # noqa: E501

        self._customer_name = customer_name

    @property
    def customer_phone(self):
        """Gets the customer_phone of this Body1.  # noqa: E501

        预订人电话  # noqa: E501

        :return: The customer_phone of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._customer_phone

    @customer_phone.setter
    def customer_phone(self, customer_phone):
        """Sets the customer_phone of this Body1.

        预订人电话  # noqa: E501

        :param customer_phone: The customer_phone of this Body1.  # noqa: E501
        :type: str
        """
        if customer_phone is None:
            raise ValueError("Invalid value for `customer_phone`, must not be `None`")  # noqa: E501

        self._customer_phone = customer_phone

    @property
    def customer_list(self):
        """Gets the customer_list of this Body1.  # noqa: E501

        入住人列表  # noqa: E501

        :return: The customer_list of this Body1.  # noqa: E501
        :rtype: list[PoiexthotelordercommitCustomerList]
        """
        return self._customer_list

    @customer_list.setter
    def customer_list(self, customer_list):
        """Sets the customer_list of this Body1.

        入住人列表  # noqa: E501

        :param customer_list: The customer_list of this Body1.  # noqa: E501
        :type: list[PoiexthotelordercommitCustomerList]
        """

        self._customer_list = customer_list

    @property
    def check_in(self):
        """Gets the check_in of this Body1.  # noqa: E501

        入住时间 yyyyMMdd  # noqa: E501

        :return: The check_in of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._check_in

    @check_in.setter
    def check_in(self, check_in):
        """Sets the check_in of this Body1.

        入住时间 yyyyMMdd  # noqa: E501

        :param check_in: The check_in of this Body1.  # noqa: E501
        :type: str
        """
        if check_in is None:
            raise ValueError("Invalid value for `check_in`, must not be `None`")  # noqa: E501

        self._check_in = check_in

    @property
    def check_out(self):
        """Gets the check_out of this Body1.  # noqa: E501

        离店时间 yyyyMMdd  # noqa: E501

        :return: The check_out of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._check_out

    @check_out.setter
    def check_out(self, check_out):
        """Sets the check_out of this Body1.

        离店时间 yyyyMMdd  # noqa: E501

        :param check_out: The check_out of this Body1.  # noqa: E501
        :type: str
        """
        if check_out is None:
            raise ValueError("Invalid value for `check_out`, must not be `None`")  # noqa: E501

        self._check_out = check_out

    @property
    def total_price(self):
        """Gets the total_price of this Body1.  # noqa: E501

        总价, 单位人民币分  # noqa: E501

        :return: The total_price of this Body1.  # noqa: E501
        :rtype: int
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this Body1.

        总价, 单位人民币分  # noqa: E501

        :param total_price: The total_price of this Body1.  # noqa: E501
        :type: int
        """
        if total_price is None:
            raise ValueError("Invalid value for `total_price`, must not be `None`")  # noqa: E501

        self._total_price = total_price

    @property
    def remark(self):
        """Gets the remark of this Body1.  # noqa: E501

        备注  # noqa: E501

        :return: The remark of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this Body1.

        备注  # noqa: E501

        :param remark: The remark of this Body1.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def date_price(self):
        """Gets the date_price of this Body1.  # noqa: E501


        :return: The date_price of this Body1.  # noqa: E501
        :rtype: list[PoiexthotelordercommitDatePrice]
        """
        return self._date_price

    @date_price.setter
    def date_price(self, date_price):
        """Sets the date_price of this Body1.


        :param date_price: The date_price of this Body1.  # noqa: E501
        :type: list[PoiexthotelordercommitDatePrice]
        """

        self._date_price = date_price

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