# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from douyin_open.Oauth2UserToken.api_client import ApiClient


class OauthCodeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def platform_oauth_connect_get(self, client_key, response_type, scope, redirect_uri, **kwargs):  # noqa: E501
        """获取授权码(code)  # noqa: E501

        注意该URL不是用来请求的, 需要展示给用户用于扫码。 在抖音APP支持端内唤醒的版本内打开的话会弹出客户端原生授权页面。  使用本接口前提: 1. 首先你需要去官网申请，使你的应用可以使用特定的Scope，具体需要哪些Scope，请查看各接口定义。 2. 其次你需要在本URL的scope字段中填上用户需要授权给你的Scope。 3. 用户授权通过后，你才可以调用相应的接口。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.platform_oauth_connect_get(client_key, response_type, scope, redirect_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str response_type: 填写code (required)
        :param str scope: 应用授权作用域,多个授权作用域以英文逗号（,）分隔 (required)
        :param str redirect_uri: 授权成功后的回调地址，必须以http/https开头。域名必须对应申请应用时填写的域名，如不清楚请联系应用申请人。 (required)
        :param str state: 用于保持请求和回调的状态
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.platform_oauth_connect_get_with_http_info(client_key, response_type, scope, redirect_uri, **kwargs)  # noqa: E501
        else:
            (data) = self.platform_oauth_connect_get_with_http_info(client_key, response_type, scope, redirect_uri, **kwargs)  # noqa: E501
            return data

    def platform_oauth_connect_get_with_http_info(self, client_key, response_type, scope, redirect_uri, **kwargs):  # noqa: E501
        """获取授权码(code)  # noqa: E501

        注意该URL不是用来请求的, 需要展示给用户用于扫码。 在抖音APP支持端内唤醒的版本内打开的话会弹出客户端原生授权页面。  使用本接口前提: 1. 首先你需要去官网申请，使你的应用可以使用特定的Scope，具体需要哪些Scope，请查看各接口定义。 2. 其次你需要在本URL的scope字段中填上用户需要授权给你的Scope。 3. 用户授权通过后，你才可以调用相应的接口。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.platform_oauth_connect_get_with_http_info(client_key, response_type, scope, redirect_uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str response_type: 填写code (required)
        :param str scope: 应用授权作用域,多个授权作用域以英文逗号（,）分隔 (required)
        :param str redirect_uri: 授权成功后的回调地址，必须以http/https开头。域名必须对应申请应用时填写的域名，如不清楚请联系应用申请人。 (required)
        :param str state: 用于保持请求和回调的状态
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'response_type', 'scope', 'redirect_uri', 'state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method platform_oauth_connect_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params or
                params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `platform_oauth_connect_get`")  # noqa: E501
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `platform_oauth_connect_get`")  # noqa: E501
        # verify the required parameter 'scope' is set
        if ('scope' not in params or
                params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `platform_oauth_connect_get`")  # noqa: E501
        # verify the required parameter 'redirect_uri' is set
        if ('redirect_uri' not in params or
                params['redirect_uri'] is None):
            raise ValueError("Missing the required parameter `redirect_uri` when calling `platform_oauth_connect_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_key' in params:
            query_params.append(('client_key', params['client_key']))  # noqa: E501
        if 'response_type' in params:
            query_params.append(('response_type', params['response_type']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501
        if 'redirect_uri' in params:
            query_params.append(('redirect_uri', params['redirect_uri']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/platform/oauth/connect/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
