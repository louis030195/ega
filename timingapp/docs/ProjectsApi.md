# timingapp.ProjectsApi

All URIs are relative to *https://web.timingapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_projects_get**](ProjectsApi.md#api_v1_projects_get) | **GET** /api/v1/projects | Return a list containing all projects.
[**api_v1_projects_hierarchy_get**](ProjectsApi.md#api_v1_projects_hierarchy_get) | **GET** /api/v1/projects/hierarchy | Return the complete project hierarchy.
[**api_v1_projects_post**](ProjectsApi.md#api_v1_projects_post) | **POST** /api/v1/projects | Create a new project.
[**api_v1_projects_project_id_delete**](ProjectsApi.md#api_v1_projects_project_id_delete) | **DELETE** /api/v1/projects/{project_id} | Delete the specified project and all of its children.
[**api_v1_projects_project_id_get**](ProjectsApi.md#api_v1_projects_project_id_get) | **GET** /api/v1/projects/{project_id} | Display the specified project.
[**api_v1_projects_project_id_put**](ProjectsApi.md#api_v1_projects_project_id_put) | **PUT** /api/v1/projects/{project_id} | Update the specified project.


# **api_v1_projects_get**
> ApiV1ProjectsGet200Response api_v1_projects_get()

Return a list containing all projects.

<br>See [Display the specified project.](#display-the-specified-project) for the returned attributes.

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import projects_api
from timingapp.model.api_v1_projects_get200_response import ApiV1ProjectsGet200Response
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
    api_instance = projects_api.ProjectsApi(api_client)
    title = "root" # str | Filter for projects whose title contains all words in this parameter. The search is case-insensitive but diacritic-sensitive. (optional)
    hide_archived = "true" # str | If set to `true`, archived projects and their children will not be included in the result. (optional)
    team_id = "team_id_example" # str | The ID of the team to list projects for. Can be omitted to list the user's private projects. See [Return a list containing all the teams you are a member of.](#return-a-list-containing-all-the-teams-you-are-a-member-of) for obtaining a team ID to provide here. (optional)
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return a list containing all projects.
        api_response = api_instance.api_v1_projects_get(title=title, hide_archived=hide_archived, team_id=team_id, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Filter for projects whose title contains all words in this parameter. The search is case-insensitive but diacritic-sensitive. | [optional]
 **hide_archived** | **str**| If set to &#x60;true&#x60;, archived projects and their children will not be included in the result. | [optional]
 **team_id** | **str**| The ID of the team to list projects for. Can be omitted to list the user&#39;s private projects. See [Return a list containing all the teams you are a member of.](#return-a-list-containing-all-the-teams-you-are-a-member-of) for obtaining a team ID to provide here. | [optional]
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1ProjectsGet200Response**](ApiV1ProjectsGet200Response.md)

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

# **api_v1_projects_hierarchy_get**
> ApiV1ProjectsHierarchyGet200Response api_v1_projects_hierarchy_get()

Return the complete project hierarchy.

<br>See [Display the specified project.](#display-the-specified-project) for the returned attributes.

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import projects_api
from timingapp.model.api_v1_projects_hierarchy_get200_response import ApiV1ProjectsHierarchyGet200Response
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
    api_instance = projects_api.ProjectsApi(api_client)
    team_id = "team_id_example" # str | The ID of the team to list projects for. Can be omitted to list the user's private projects. See [Return a list containing all the teams you are a member of.](#return-a-list-containing-all-the-teams-you-are-a-member-of) for obtaining a team ID to provide here. (optional)
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return the complete project hierarchy.
        api_response = api_instance.api_v1_projects_hierarchy_get(team_id=team_id, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_hierarchy_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The ID of the team to list projects for. Can be omitted to list the user&#39;s private projects. See [Return a list containing all the teams you are a member of.](#return-a-list-containing-all-the-teams-you-are-a-member-of) for obtaining a team ID to provide here. | [optional]
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1ProjectsHierarchyGet200Response**](ApiV1ProjectsHierarchyGet200Response.md)

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

# **api_v1_projects_post**
> ApiV1ProjectsGet201Response api_v1_projects_post(api_v1_projects_get_request)

Create a new project.

<br>See [Display the specified project.](#display-the-specified-project) for the returned attributes.

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import projects_api
from timingapp.model.api_v1_projects_get201_response import ApiV1ProjectsGet201Response
from timingapp.model.api_v1_projects_get_request import ApiV1ProjectsGetRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    api_v1_projects_get_request = ApiV1ProjectsGetRequest(
        title="Acme Inc.",
/projects/1,
#FF0000,
        productivity_score=1.0,
        is_archived=False,
        team_id=1,
    ) # ApiV1ProjectsGetRequest | 
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new project.
        api_response = api_instance.api_v1_projects_post(api_v1_projects_get_request)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new project.
        api_response = api_instance.api_v1_projects_post(api_v1_projects_get_request, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_projects_get_request** | [**ApiV1ProjectsGetRequest**](ApiV1ProjectsGetRequest.md)|  |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1ProjectsGet201Response**](ApiV1ProjectsGet201Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_projects_project_id_delete**
> api_v1_projects_project_id_delete(project_id)

Delete the specified project and all of its children.



### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "" # str | Optional parameter. The ID of the project to display.
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete the specified project and all of its children.
        api_instance.api_v1_projects_project_id_delete(project_id)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_project_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete the specified project and all of its children.
        api_instance.api_v1_projects_project_id_delete(project_id, authorization=authorization, content_type=content_type, accept=accept)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_project_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Optional parameter. The ID of the project to display. |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_projects_project_id_get**
> ApiV1ProjectsProjectIdDelete200Response api_v1_projects_project_id_get(project_id)

Display the specified project.

<br>The following attributes will be returned:   - `self`: A reference to the entity itself, relative to the API root.  - `title`: The project's title.  - `title_chain`: An array containing the title of the project and all its ancestors. Example: `[\"Parent\", \"Child\"]`  - `color`: The project's color, in hexadecimal format (`#RRGGBB`). Example: `#FF0000`  - `productivity_score`: The project's productivity rating, between -1 (very unproductive) and 1 (very productive). Example: `1`  - `is_archived`: Whether the project has been archived. Defaults to false. Example: `false`  - `parent`: A reference to the enclosing project.  - `children`: The project's children.  - `team_id`: The ID of the team that this project belongs to, if applicable.  <aside class=\"notice\"> Child projects are provided as references; i.e. they only contain the <code>self</code> attribute. </aside>

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import projects_api
from timingapp.model.api_v1_projects_project_id_delete200_response import ApiV1ProjectsProjectIdDelete200Response
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "" # str | Optional parameter. The ID of the project to display.
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Display the specified project.
        api_response = api_instance.api_v1_projects_project_id_get(project_id)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_project_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Display the specified project.
        api_response = api_instance.api_v1_projects_project_id_get(project_id, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_project_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Optional parameter. The ID of the project to display. |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1ProjectsProjectIdDelete200Response**](ApiV1ProjectsProjectIdDelete200Response.md)

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

# **api_v1_projects_project_id_put**
> ApiV1ProjectsProjectIdDelete200Response1 api_v1_projects_project_id_put(project_id)

Update the specified project.

<br>See [Display the specified project.](#display-the-specified-project) for the returned attributes.  <aside class=\"notice\"> Omitted fields will not be updated, even when using the `PUT` method. </aside>  <aside class=\"notice\"> Changing a project's parent or children is currently not possible. </aside>

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import projects_api
from timingapp.model.api_v1_projects_project_id_delete_request import ApiV1ProjectsProjectIdDeleteRequest
from timingapp.model.api_v1_projects_project_id_delete200_response1 import ApiV1ProjectsProjectIdDelete200Response1
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "" # str | Optional parameter. The ID of the project to display.
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)
    api_v1_projects_project_id_delete_request = ApiV1ProjectsProjectIdDeleteRequest(
        title="Acme Inc.",
#FF0000,
        productivity_score=1.0,
        is_archived=False,
    ) # ApiV1ProjectsProjectIdDeleteRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the specified project.
        api_response = api_instance.api_v1_projects_project_id_put(project_id)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_project_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the specified project.
        api_response = api_instance.api_v1_projects_project_id_put(project_id, authorization=authorization, content_type=content_type, accept=accept, api_v1_projects_project_id_delete_request=api_v1_projects_project_id_delete_request)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_project_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Optional parameter. The ID of the project to display. |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]
 **api_v1_projects_project_id_delete_request** | [**ApiV1ProjectsProjectIdDeleteRequest**](ApiV1ProjectsProjectIdDeleteRequest.md)|  | [optional]

### Return type

[**ApiV1ProjectsProjectIdDelete200Response1**](ApiV1ProjectsProjectIdDelete200Response1.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

