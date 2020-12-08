# coding: utf-8

"""
    团购活动用户申请退款订单列表

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from douyin_open.EnterpriseGrouponGrouponOrderOrderApplyRefundList.api_client import ApiClient


class EnterpriseGrouponOrderRefundListApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def enterprise_groupon_order_refund_apply_list_get(self, access_token, open_id, count, start_time, end_time, **kwargs):  # noqa: E501
        """团购活动用户申请退款订单列表  # noqa: E501

        * Scope: `enterprise.groupon`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enterprise_groupon_order_refund_apply_list_get(access_token, open_id, count, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param int count: 每页数量 (required)
        :param int start_time: 退款申请开始时间，unix时间戳 (required)
        :param int end_time: 退款申请结束时间，unix时间戳 (required)
        :param int cursor: 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。
        :param int status: * 状态筛选   * 1: 待确认   * 2: 已确认 
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enterprise_groupon_order_refund_apply_list_get_with_http_info(access_token, open_id, count, start_time, end_time, **kwargs)  # noqa: E501
        else:
            (data) = self.enterprise_groupon_order_refund_apply_list_get_with_http_info(access_token, open_id, count, start_time, end_time, **kwargs)  # noqa: E501
            return data

    def enterprise_groupon_order_refund_apply_list_get_with_http_info(self, access_token, open_id, count, start_time, end_time, **kwargs):  # noqa: E501
        """团购活动用户申请退款订单列表  # noqa: E501

        * Scope: `enterprise.groupon`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enterprise_groupon_order_refund_apply_list_get_with_http_info(access_token, open_id, count, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param int count: 每页数量 (required)
        :param int start_time: 退款申请开始时间，unix时间戳 (required)
        :param int end_time: 退款申请结束时间，unix时间戳 (required)
        :param int cursor: 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。
        :param int status: * 状态筛选   * 1: 待确认   * 2: 已确认 
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'open_id', 'count', 'start_time', 'end_time', 'cursor', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enterprise_groupon_order_refund_apply_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `enterprise_groupon_order_refund_apply_list_get`")  # noqa: E501
        # verify the required parameter 'open_id' is set
        if ('open_id' not in params or
                params['open_id'] is None):
            raise ValueError("Missing the required parameter `open_id` when calling `enterprise_groupon_order_refund_apply_list_get`")  # noqa: E501
        # verify the required parameter 'count' is set
        if ('count' not in params or
                params['count'] is None):
            raise ValueError("Missing the required parameter `count` when calling `enterprise_groupon_order_refund_apply_list_get`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params or
                params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `enterprise_groupon_order_refund_apply_list_get`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params or
                params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `enterprise_groupon_order_refund_apply_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'open_id' in params:
            query_params.append(('open_id', params['open_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/groupon/order/refund/apply/list/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
