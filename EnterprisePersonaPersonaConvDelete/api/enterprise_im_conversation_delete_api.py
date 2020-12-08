# coding: utf-8

"""
    客服会话删除

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from douyin_open.EnterprisePersonaPersonaConvDelete.api_client import ApiClient


class EnterpriseImConversationDeleteApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def enterprise_im_persona_conversation_delete_post(self, body, open_id, access_token, **kwargs):  # noqa: E501
        """删除客服会话  # noqa: E501

        * Scope: `enterprise.im`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enterprise_im_persona_conversation_delete_post(body, open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: (required)
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enterprise_im_persona_conversation_delete_post_with_http_info(body, open_id, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.enterprise_im_persona_conversation_delete_post_with_http_info(body, open_id, access_token, **kwargs)  # noqa: E501
            return data

    def enterprise_im_persona_conversation_delete_post_with_http_info(self, body, open_id, access_token, **kwargs):  # noqa: E501
        """删除客服会话  # noqa: E501

        * Scope: `enterprise.im`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enterprise_im_persona_conversation_delete_post_with_http_info(body, open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: (required)
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'open_id', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enterprise_im_persona_conversation_delete_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `enterprise_im_persona_conversation_delete_post`")  # noqa: E501
        # verify the required parameter 'open_id' is set
        if ('open_id' not in params or
                params['open_id'] is None):
            raise ValueError("Missing the required parameter `open_id` when calling `enterprise_im_persona_conversation_delete_post`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `enterprise_im_persona_conversation_delete_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'open_id' in params:
            query_params.append(('open_id', params['open_id']))  # noqa: E501
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/im/persona/conversation/delete/', 'POST',
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
