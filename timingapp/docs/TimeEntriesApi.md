# timingapp.TimeEntriesApi

All URIs are relative to *https://web.timingapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_time_entries_activity_id_delete**](TimeEntriesApi.md#api_v1_time_entries_activity_id_delete) | **DELETE** /api/v1/time-entries/{activity_id} | Delete the specified time entry.
[**api_v1_time_entries_activity_id_get**](TimeEntriesApi.md#api_v1_time_entries_activity_id_get) | **GET** /api/v1/time-entries/{activity_id} | Display the specified time entry.
[**api_v1_time_entries_activity_id_put**](TimeEntriesApi.md#api_v1_time_entries_activity_id_put) | **PUT** /api/v1/time-entries/{activity_id} | Update the specified time entry.
[**api_v1_time_entries_get**](TimeEntriesApi.md#api_v1_time_entries_get) | **GET** /api/v1/time-entries | Return a list of time entries.
[**api_v1_time_entries_post**](TimeEntriesApi.md#api_v1_time_entries_post) | **POST** /api/v1/time-entries | Create a new time entry.
[**api_v1_time_entries_start_post**](TimeEntriesApi.md#api_v1_time_entries_start_post) | **POST** /api/v1/time-entries/start | Start a new timer.
[**api_v1_time_entries_stop_put**](TimeEntriesApi.md#api_v1_time_entries_stop_put) | **PUT** /api/v1/time-entries/stop | Stop the currently running timer.


# **api_v1_time_entries_activity_id_delete**
> api_v1_time_entries_activity_id_delete(activity_id)

Delete the specified time entry.



### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import time_entries_api
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
    api_instance = time_entries_api.TimeEntriesApi(api_client)
    activity_id = "" # str | Optional parameter. The ID of the activity to display.
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete the specified time entry.
        api_instance.api_v1_time_entries_activity_id_delete(activity_id)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_activity_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete the specified time entry.
        api_instance.api_v1_time_entries_activity_id_delete(activity_id, authorization=authorization, content_type=content_type, accept=accept)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_activity_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| Optional parameter. The ID of the activity to display. |
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

# **api_v1_time_entries_activity_id_get**
> ApiV1TimeEntriesActivityIdDelete200Response api_v1_time_entries_activity_id_get(activity_id)

Display the specified time entry.

<br>The following attributes will be returned:   - `self`: A link to the entity itself, relative to the API root.  - `start_date`: The time entry's start date and time.  - `end_date`: The time entry's end date and time.  - `duration`: The time entry's total duration, in seconds.  - `project`: The project this time entry is associated with.  - `title`: The time entry's title.  - `notes`: The time entry's notes.  - `is_running`: Whether the time entry is currently running. Only one time entry can be running at any given time.

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import time_entries_api
from timingapp.model.api_v1_time_entries_activity_id_delete200_response import ApiV1TimeEntriesActivityIdDelete200Response
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
    api_instance = time_entries_api.TimeEntriesApi(api_client)
    activity_id = "" # str | Optional parameter. The ID of the activity to display.
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Display the specified time entry.
        api_response = api_instance.api_v1_time_entries_activity_id_get(activity_id)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_activity_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Display the specified time entry.
        api_response = api_instance.api_v1_time_entries_activity_id_get(activity_id, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_activity_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| Optional parameter. The ID of the activity to display. |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1TimeEntriesActivityIdDelete200Response**](ApiV1TimeEntriesActivityIdDelete200Response.md)

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

# **api_v1_time_entries_activity_id_put**
> ApiV1TimeEntriesActivityIdDelete200Response1 api_v1_time_entries_activity_id_put(activity_id)

Update the specified time entry.

<br>See [Display the specified time entry.](#display-the-specified-time-entry) for the returned attributes.  <aside class=\"notice\"> Omitted fields will not be updated, even when using the `PUT` method. </aside>  <aside class=\"notice\"> A time entry's title and project fields can not both be empty. </aside>

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import time_entries_api
from timingapp.model.api_v1_time_entries_activity_id_delete_request import ApiV1TimeEntriesActivityIdDeleteRequest
from timingapp.model.api_v1_time_entries_activity_id_delete200_response1 import ApiV1TimeEntriesActivityIdDelete200Response1
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
    api_instance = time_entries_api.TimeEntriesApi(api_client)
    activity_id = "" # str | Optional parameter. The ID of the activity to display.
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)
    api_v1_time_entries_activity_id_delete_request = ApiV1TimeEntriesActivityIdDeleteRequest(
2019-01-01T00:00:00+00:00,
2019-01-01T01:00:00+00:00,
Unproductive child project,
        title="Client Meeting",
        notes="Some more detailed notes",
    ) # ApiV1TimeEntriesActivityIdDeleteRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the specified time entry.
        api_response = api_instance.api_v1_time_entries_activity_id_put(activity_id)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_activity_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the specified time entry.
        api_response = api_instance.api_v1_time_entries_activity_id_put(activity_id, authorization=authorization, content_type=content_type, accept=accept, api_v1_time_entries_activity_id_delete_request=api_v1_time_entries_activity_id_delete_request)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_activity_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| Optional parameter. The ID of the activity to display. |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]
 **api_v1_time_entries_activity_id_delete_request** | [**ApiV1TimeEntriesActivityIdDeleteRequest**](ApiV1TimeEntriesActivityIdDeleteRequest.md)|  | [optional]

### Return type

[**ApiV1TimeEntriesActivityIdDelete200Response1**](ApiV1TimeEntriesActivityIdDelete200Response1.md)

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

# **api_v1_time_entries_get**
> ApiV1TimeEntriesGet200Response api_v1_time_entries_get()

Return a list of time entries.

<br>See [Display the specified time entry.](#display-the-specified-time-entry) for the returned attributes.  Items are ordered descending by their `start_date` field.  <aside class=\"notice\"> If no date range filter is provided by setting <em>both</em> `start_date_min` <em>and</em> `start_date_max`, this query returns all time entries between midnight (UTC) 30 days ago and end of day (UTC) today. </aside>

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import time_entries_api
from timingapp.model.api_v1_time_entries_get200_response import ApiV1TimeEntriesGet200Response
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
    api_instance = time_entries_api.TimeEntriesApi(api_client)
    start_date_min = "2019-01-01T00:00:00+00:00" # str | Restricts the query to time entries whose start date is equal to or later than this parameter. (optional)
    start_date_max = "2019-01-01T23:59:59+00:00" # str | Restricts the query to time entries whose start date is equal to or earlier than this parameter. (optional)
    projects = "/projects/1" # str | Restricts the query to time entries associated with the given project. Can be repeated to include time entries from several projects. If you would like to include time entries that are not assigned to any project, you can provide an empty string, i.e. `projects[]=` (optional)
    include_child_projects = "1" # str | If true, the response will also contain time entries that belong to any child projects of the ones provided in `projects[]`. Default: `0` (optional)
    search_query = "meeting" # str | Restricts the query to time entries whose title and/or notes contain all words in this parameter. The search is case-insensitive but diacritic-sensitive. (optional)
    is_running = "0" # str | If provided, returns only time entries that are either running or not running. (optional)
    include_project_data = "1" # str | If true, the properties of the time entry's project will be included in the response. Default: `0` (optional)
    include_team_members = "0" # str | If true, the response will also contain time entries that belong to other team members, provided the current user has permission to view them. Default: `0` (optional)
    team_members = "/users/1" # str | Restricts the query to data associated with the given user. Can be repeated to include time entries from several users. (optional)
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return a list of time entries.
        api_response = api_instance.api_v1_time_entries_get(start_date_min=start_date_min, start_date_max=start_date_max, projects=projects, include_child_projects=include_child_projects, search_query=search_query, is_running=is_running, include_project_data=include_project_data, include_team_members=include_team_members, team_members=team_members, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_min** | **str**| Restricts the query to time entries whose start date is equal to or later than this parameter. | [optional]
 **start_date_max** | **str**| Restricts the query to time entries whose start date is equal to or earlier than this parameter. | [optional]
 **projects** | **str**| Restricts the query to time entries associated with the given project. Can be repeated to include time entries from several projects. If you would like to include time entries that are not assigned to any project, you can provide an empty string, i.e. &#x60;projects[]&#x3D;&#x60; | [optional]
 **include_child_projects** | **str**| If true, the response will also contain time entries that belong to any child projects of the ones provided in &#x60;projects[]&#x60;. Default: &#x60;0&#x60; | [optional]
 **search_query** | **str**| Restricts the query to time entries whose title and/or notes contain all words in this parameter. The search is case-insensitive but diacritic-sensitive. | [optional]
 **is_running** | **str**| If provided, returns only time entries that are either running or not running. | [optional]
 **include_project_data** | **str**| If true, the properties of the time entry&#39;s project will be included in the response. Default: &#x60;0&#x60; | [optional]
 **include_team_members** | **str**| If true, the response will also contain time entries that belong to other team members, provided the current user has permission to view them. Default: &#x60;0&#x60; | [optional]
 **team_members** | **str**| Restricts the query to data associated with the given user. Can be repeated to include time entries from several users. | [optional]
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1TimeEntriesGet200Response**](ApiV1TimeEntriesGet200Response.md)

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

# **api_v1_time_entries_post**
> ApiV1TimeEntriesGet201Response api_v1_time_entries_post(api_v1_time_entries_get_request)

Create a new time entry.

<br>See [Display the specified time entry.](#display-the-specified-time-entry) for the returned attributes.  <aside class=\"notice\"> The title and project fields can not both be empty. </aside>

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import time_entries_api
from timingapp.model.api_v1_time_entries_get201_response import ApiV1TimeEntriesGet201Response
from timingapp.model.api_v1_time_entries_get_request import ApiV1TimeEntriesGetRequest
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
    api_instance = time_entries_api.TimeEntriesApi(api_client)
    api_v1_time_entries_get_request = ApiV1TimeEntriesGetRequest(
2019-01-01T00:00:00+00:00,
2019-01-01T01:00:00+00:00,
Unproductive child project,
        title="Client Meeting",
        notes="Some more detailed notes",
    ) # ApiV1TimeEntriesGetRequest | 
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new time entry.
        api_response = api_instance.api_v1_time_entries_post(api_v1_time_entries_get_request)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new time entry.
        api_response = api_instance.api_v1_time_entries_post(api_v1_time_entries_get_request, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_time_entries_get_request** | [**ApiV1TimeEntriesGetRequest**](ApiV1TimeEntriesGetRequest.md)|  |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1TimeEntriesGet201Response**](ApiV1TimeEntriesGet201Response.md)

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

# **api_v1_time_entries_start_post**
> ApiV1TimeEntriesStartPost201Response api_v1_time_entries_start_post()

Start a new timer.

<br>This also stops the currently running timer if there is one.  See [Display the specified time entry.](#display-the-specified-time-entry) for the returned attributes.  <aside class=\"notice\"> The title and project fields can not both be empty. </aside>

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import time_entries_api
from timingapp.model.api_v1_time_entries_start_post201_response import ApiV1TimeEntriesStartPost201Response
from timingapp.model.api_v1_time_entries_start_post_request import ApiV1TimeEntriesStartPostRequest
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
    api_instance = time_entries_api.TimeEntriesApi(api_client)
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)
    api_v1_time_entries_start_post_request = ApiV1TimeEntriesStartPostRequest(
2019-01-01T00:00:00+00:00,
Unproductive child project,
        title="Client Meeting",
        notes="Some more detailed notes",
    ) # ApiV1TimeEntriesStartPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a new timer.
        api_response = api_instance.api_v1_time_entries_start_post(authorization=authorization, content_type=content_type, accept=accept, api_v1_time_entries_start_post_request=api_v1_time_entries_start_post_request)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_start_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]
 **api_v1_time_entries_start_post_request** | [**ApiV1TimeEntriesStartPostRequest**](ApiV1TimeEntriesStartPostRequest.md)|  | [optional]

### Return type

[**ApiV1TimeEntriesStartPost201Response**](ApiV1TimeEntriesStartPost201Response.md)

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

# **api_v1_time_entries_stop_put**
> ApiV1TimeEntriesStopPut200Response api_v1_time_entries_stop_put()

Stop the currently running timer.

<br>Returns the stopped timer's attributes as listed under [Display the specified time entry.](#display-the-specified-time-entry).

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import time_entries_api
from timingapp.model.api_v1_time_entries_stop_put200_response import ApiV1TimeEntriesStopPut200Response
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
    api_instance = time_entries_api.TimeEntriesApi(api_client)
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop the currently running timer.
        api_response = api_instance.api_v1_time_entries_stop_put(authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling TimeEntriesApi->api_v1_time_entries_stop_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1TimeEntriesStopPut200Response**](ApiV1TimeEntriesStopPut200Response.md)

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

