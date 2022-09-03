# timingapp.TeamsApi

All URIs are relative to *https://web.timingapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_teams_get**](TeamsApi.md#api_v1_teams_get) | **GET** /api/v1/teams | Return a list containing all the teams you are a member of.
[**api_v1_teams_team_id_members_get**](TeamsApi.md#api_v1_teams_team_id_members_get) | **GET** /api/v1/teams/{team_id}/members | Return a list containing all active members of the given team.


# **api_v1_teams_get**
> ApiV1TeamsGet200Response api_v1_teams_get()

Return a list containing all the teams you are a member of.



### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import teams_api
from timingapp.model.api_v1_teams_get200_response import ApiV1TeamsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://web.timingapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = timingapp.Configuration(
    host = "https://web.timingapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: default
configuration = timingapp.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with timingapp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return a list containing all the teams you are a member of.
        api_response = api_instance.api_v1_teams_get(authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TeamsApi->api_v1_teams_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1TeamsGet200Response**](ApiV1TeamsGet200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_teams_team_id_members_get**
> ApiV1TeamsTeamIdMembersGet200Response api_v1_teams_team_id_members_get(team_id)

Return a list containing all active members of the given team.

<br>Members with pending invitations will be excluded.  The following attributes will be returned:   - `self`: A reference to the entity itself, relative to the API root.  - `email`: The team member's email address.  - `name`: The team member's name. May be null if the team member has not entered a name in their account profile.

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import teams_api
from timingapp.model.api_v1_teams_team_id_members_get200_response import ApiV1TeamsTeamIdMembersGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://web.timingapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = timingapp.Configuration(
    host = "https://web.timingapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: default
configuration = timingapp.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with timingapp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)
    team_id = "" # str | Optional parameter. The ID of the team to list members for.
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return a list containing all active members of the given team.
        api_response = api_instance.api_v1_teams_team_id_members_get(team_id)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TeamsApi->api_v1_teams_team_id_members_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return a list containing all active members of the given team.
        api_response = api_instance.api_v1_teams_team_id_members_get(team_id, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TeamsApi->api_v1_teams_team_id_members_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Optional parameter. The ID of the team to list members for. |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1TeamsTeamIdMembersGet200Response**](ApiV1TeamsTeamIdMembersGet200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

