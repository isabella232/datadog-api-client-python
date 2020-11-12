# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v1.api_client import ApiClient, Endpoint
from datadog_api_client.v1.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from datadog_api_client.v1.model.api_error_response import APIErrorResponse
from datadog_api_client.v1.model.host_tags import HostTags
from datadog_api_client.v1.model.tag_to_hosts import TagToHosts


class TagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_host_tags(
            self,
            host_name,
            body,
            **kwargs
        ):
            """Add tags to a host  # noqa: E501

            This endpoint allows you to add new tags to a host, optionally specifying where these tags come from.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_host_tags(host_name, body, async_req=True)
            >>> result = thread.get()

            Args:
                host_name (str): This endpoint allows you to add new tags to a host, optionally specifying where the tags came from.
                body (HostTags): Update host tags request body.

            Keyword Args:
                source (str): The source of the tags. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                HostTags
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['host_name'] = \
                host_name
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.create_host_tags = Endpoint(
            settings={
                'response_type': (HostTags,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v1/tags/hosts/{host_name}',
                'operation_id': 'create_host_tags',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_name',
                    'body',
                    'source',
                ],
                'required': [
                    'host_name',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_name':
                        (str,),
                    'body':
                        (HostTags,),
                    'source':
                        (str,),
                },
                'attribute_map': {
                    'host_name': 'host_name',
                    'source': 'source',
                },
                'location_map': {
                    'host_name': 'path',
                    'body': 'body',
                    'source': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_host_tags
        )

        def __delete_host_tags(
            self,
            host_name,
            **kwargs
        ):
            """Remove host tags  # noqa: E501

            This endpoint allows you to remove all user-assigned tags for a single host.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_host_tags(host_name, async_req=True)
            >>> result = thread.get()

            Args:
                host_name (str): This endpoint allows you to remove all user-assigned tags for a single host.

            Keyword Args:
                source (str): The source of the tags (e.g. chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['host_name'] = \
                host_name
            return self.call_with_http_info(**kwargs)

        self.delete_host_tags = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v1/tags/hosts/{host_name}',
                'operation_id': 'delete_host_tags',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_name',
                    'source',
                ],
                'required': [
                    'host_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_name':
                        (str,),
                    'source':
                        (str,),
                },
                'attribute_map': {
                    'host_name': 'host_name',
                    'source': 'source',
                },
                'location_map': {
                    'host_name': 'path',
                    'source': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_host_tags
        )

        def __get_host_tags(
            self,
            host_name,
            **kwargs
        ):
            """Get host tags  # noqa: E501

            Return the list of tags that apply to a given host.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_host_tags(host_name, async_req=True)
            >>> result = thread.get()

            Args:
                host_name (str): When specified, filters list of tags to those tags with the specified source.

            Keyword Args:
                source (str): Source to filter.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                HostTags
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['host_name'] = \
                host_name
            return self.call_with_http_info(**kwargs)

        self.get_host_tags = Endpoint(
            settings={
                'response_type': (HostTags,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v1/tags/hosts/{host_name}',
                'operation_id': 'get_host_tags',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_name',
                    'source',
                ],
                'required': [
                    'host_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_name':
                        (str,),
                    'source':
                        (str,),
                },
                'attribute_map': {
                    'host_name': 'host_name',
                    'source': 'source',
                },
                'location_map': {
                    'host_name': 'path',
                    'source': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_host_tags
        )

        def __list_host_tags(
            self,
            **kwargs
        ):
            """Get Tags  # noqa: E501

            Return a mapping of tags to hosts for your whole infrastructure.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_host_tags(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                source (str): When specified, filters host list to those tags with the specified source.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TagToHosts
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_host_tags = Endpoint(
            settings={
                'response_type': (TagToHosts,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v1/tags/hosts',
                'operation_id': 'list_host_tags',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'source',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'source':
                        (str,),
                },
                'attribute_map': {
                    'source': 'source',
                },
                'location_map': {
                    'source': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_host_tags
        )

        def __update_host_tags(
            self,
            host_name,
            body,
            **kwargs
        ):
            """Update host tags  # noqa: E501

            This endpoint allows you to update/replace all tags in an integration source with those supplied in the request.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_host_tags(host_name, body, async_req=True)
            >>> result = thread.get()

            Args:
                host_name (str): This endpoint allows you to update/replace all in an integration source with those supplied in the request.
                body (HostTags): Add tags to host

            Keyword Args:
                source (str): The source of the tags (e.g. chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                HostTags
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['host_name'] = \
                host_name
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_host_tags = Endpoint(
            settings={
                'response_type': (HostTags,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v1/tags/hosts/{host_name}',
                'operation_id': 'update_host_tags',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_name',
                    'body',
                    'source',
                ],
                'required': [
                    'host_name',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_name':
                        (str,),
                    'body':
                        (HostTags,),
                    'source':
                        (str,),
                },
                'attribute_map': {
                    'host_name': 'host_name',
                    'source': 'source',
                },
                'location_map': {
                    'host_name': 'path',
                    'body': 'body',
                    'source': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_host_tags
        )