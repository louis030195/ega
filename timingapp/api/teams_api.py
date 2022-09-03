"""
    API Reference

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from timingapp.api_client import ApiClient, Endpoint as _Endpoint
from timingapp.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from timingapp.model.api_v1_teams_get200_response import ApiV1TeamsGet200Response
from timingapp.model.api_v1_teams_team_id_members_get200_response import ApiV1TeamsTeamIdMembersGet200Response


class TeamsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.api_v1_teams_get_endpoint = _Endpoint(
            settings={
                'response_type': (ApiV1TeamsGet200Response,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/api/v1/teams',
                'operation_id': 'api_v1_teams_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'authorization',
                    'content_type',
                    'accept',
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
                    'authorization':
                        (str,),
                    'content_type':
                        (str,),
                    'accept':
                        (str,),
                },
                'attribute_map': {
                    'authorization': 'Authorization',
                    'content_type': 'Content-Type',
                    'accept': 'Accept',
                },
                'location_map': {
                    'authorization': 'header',
                    'content_type': 'header',
                    'accept': 'header',
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
            api_client=api_client
        )
        self.api_v1_teams_team_id_members_get_endpoint = _Endpoint(
            settings={
                'response_type': (ApiV1TeamsTeamIdMembersGet200Response,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/api/v1/teams/{team_id}/members',
                'operation_id': 'api_v1_teams_team_id_members_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'team_id',
                    'authorization',
                    'content_type',
                    'accept',
                ],
                'required': [
                    'team_id',
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
                    'team_id':
                        (str,),
                    'authorization':
                        (str,),
                    'content_type':
                        (str,),
                    'accept':
                        (str,),
                },
                'attribute_map': {
                    'team_id': 'team_id',
                    'authorization': 'Authorization',
                    'content_type': 'Content-Type',
                    'accept': 'Accept',
                },
                'location_map': {
                    'team_id': 'path',
                    'authorization': 'header',
                    'content_type': 'header',
                    'accept': 'header',
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
            api_client=api_client
        )

    def api_v1_teams_get(
        self,
        **kwargs
    ):
        """Return a list containing all the teams you are a member of.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_teams_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            authorization (str): . [optional]
            content_type (str): . [optional]
            accept (str): . [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ApiV1TeamsGet200Response
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.api_v1_teams_get_endpoint.call_with_http_info(**kwargs)

    def api_v1_teams_team_id_members_get(
        self,
        team_id,
        **kwargs
    ):
        """Return a list containing all active members of the given team.  # noqa: E501

        <br>Members with pending invitations will be excluded.  The following attributes will be returned:   - `self`: A reference to the entity itself, relative to the API root.  - `email`: The team member's email address.  - `name`: The team member's name. May be null if the team member has not entered a name in their account profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_teams_team_id_members_get(team_id, async_req=True)
        >>> result = thread.get()

        Args:
            team_id (str): Optional parameter. The ID of the team to list members for.

        Keyword Args:
            authorization (str): . [optional]
            content_type (str): . [optional]
            accept (str): . [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ApiV1TeamsTeamIdMembersGet200Response
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['team_id'] = \
            team_id
        return self.api_v1_teams_team_id_members_get_endpoint.call_with_http_info(**kwargs)

