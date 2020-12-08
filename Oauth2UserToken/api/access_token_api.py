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


class AccessTokenApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def oauth_access_token_get(self, client_key, client_secret, code, grant_type, **kwargs):  # noqa: E501
        """获取access_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_access_token_get(client_key, client_secret, code, grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str client_secret: 应用唯一标识对应的密钥 (required)
        :param str code: 授权码 (required)
        :param str grant_type: 写死\"authorization_code\"即可 (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth_access_token_get_with_http_info(client_key, client_secret, code, grant_type, **kwargs)  # noqa: E501
        else:
            (data) = self.oauth_access_token_get_with_http_info(client_key, client_secret, code, grant_type, **kwargs)  # noqa: E501
            return data

    def oauth_access_token_get_with_http_info(self, client_key, client_secret, code, grant_type, **kwargs):  # noqa: E501
        """获取access_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_access_token_get_with_http_info(client_key, client_secret, code, grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_key: 应用唯一标识 (required)
        :param str client_secret: 应用唯一标识对应的密钥 (required)
        :param str code: 授权码 (required)
        :param str grant_type: 写死\"authorization_code\"即可 (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'client_secret', 'code', 'grant_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_access_token_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params or
                params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `oauth_access_token_get`")  # noqa: E501
        # verify the required parameter 'client_secret' is set
        if ('client_secret' not in params or
                params['client_secret'] is None):
            raise ValueError("Missing the required parameter `client_secret` when calling `oauth_access_token_get`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `oauth_access_token_get`")  # noqa: E501
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params or
                params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `oauth_access_token_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_key' in params:
            query_params.append(('client_key', params['client_key']))  # noqa: E501
        if 'client_secret' in params:
            query_params.append(('client_secret', params['client_secret']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'grant_type' in params:
            query_params.append(('grant_type', params['grant_type']))  # noqa: E501

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
            '/oauth/access_token/', 'GET',
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
