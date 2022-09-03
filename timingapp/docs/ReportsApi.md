# timingapp.ReportsApi

All URIs are relative to *https://web.timingapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_report_get**](ReportsApi.md#api_v1_report_get) | **GET** /api/v1/report | Generate a report that can contain both time entries and app usage.


# **api_v1_report_get**
> ApiV1ReportGet200Response api_v1_report_get()

Generate a report that can contain both time entries and app usage.

<br>Returns a JSON array with several rows; each row includes the total duration (in seconds) belonging to the corresponding other (configurable) columns.  The `include_app_usage` and `include_team_members` parameters govern whether to include app usage (otherwise, only time entries are returned) as well as data for other team members. <br>The `start_date_min`, `start_date_max`, `projects`(also see `include_child_projects`) and `search_query` parameters allow filtering the returned data. <br>The `columns`, `project_grouping_level`, `include_project_data`, `timespan_grouping_mode`, and `sort` parameters govern the presentation of the returned data.  <aside class=\"notice\"> Fetching large amounts of app usage can put a substantial amount of load on our servers, so please be mindful before frequently requesting large amounts of data using this API. </aside>  <aside class=\"notice\"> If no date range filter is provided by setting <em>both</em> `start_date_min` <em>and</em> `start_date_max`, this query returns all time entries between midnight (UTC) 30 days ago and end of day (UTC) today. </aside>

### Example

* Bearer Authentication (default):

```python
import time
import timingapp
from timingapp.api import reports_api
from timingapp.model.api_v1_report_get200_response import ApiV1ReportGet200Response
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
    api_instance = reports_api.ReportsApi(api_client)
    include_app_usage = "0" # str | Whether to include app usage in the report. If false, only time entries are returned. Default: `0` (optional)
    include_team_members = "0" # str | If true, the response will also contain time entries that belong to other team members, provided the current user has permission to view them. Default: `0` (optional)
    team_members = "/users/1" # str | Restricts the query to data associated with the given user. Can be repeated to include time entries from several users. (optional)
    start_date_min = "2019-01-01T00:00:00+00:00" # str | Restricts the query to data whose start date is equal to or later than this parameter. (optional)
    start_date_max = "2019-01-01T23:59:59+00:00" # str | Restricts the query to data whose start date is equal to or earlier than this parameter. (optional)
    projects = "/projects/1" # str | Restricts the query to data associated with the given project. Can be repeated to include time entries from several projects. If you would like to include time entries that are not assigned to any project, you can provide an empty string, i.e. `projects[]=` (optional)
    include_child_projects = "1" # str | If true, the response will also contain time entries that belong to any child projects of the ones provided in `projects[]`. Default: `0` (optional)
    search_query = "meeting" # str | Restricts the query to time entries whose title and/or notes contain all words in this parameter. The search is case-insensitive but diacritic-sensitive. Note: this parameter can not be used when app usage is included. (optional)
    columns = "project" # str | Which columns to show. The `user` column is ignored if `include_team_members` is false. Possible values: `project`, `title`, `notes`, `timespan`, `user`. Default: `user`, `project`, `title`. `start_date` and `end_date` is shown when `timespan` column is sent. (optional)
    project_grouping_level = 0 # int | When this argument is provided, report lines for projects below the given level will be aggregated by their parent project on the given level. For example, when `project_grouping_level` is 0, all times in sub-projects will be counted towards the corresponding project on the \"root\" (i.e. highest) level in the project tree. Can be a non-negative integer or -1. The default is -1, which indicates no grouping (i.e. all projects will be returned, regardless of how deep they are in the hierarchy). Requires `columns[]` to contain `project`. (optional)
    include_project_data = "1" # str | If true, the properties of each line's project will be included in the response. Requires `columns[]` to contain `project`. (optional)
    timespan_grouping_mode = "day" # str | When this argument is provided, report lines will be aggregated according to the given calendar unit. Possible values: `exact`, `day`, `week`, `month`, `year`. Default: `exact` (optional)
    sort = "-duration" # str | Sort the results by the given column. Prepend column name with a dash (`-`) to sort descending. Default: `-duration`. Examples: `sort[]=-duration` -> Sort descending by duration. `sort[]=user&sort[]=-duration` -> Sort ascending by user, then descending by duration. (optional)
    authorization = "Bearer {{token}}" # str |  (optional)
    content_type = "application/json" # str |  (optional)
    accept = "application/json" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate a report that can contain both time entries and app usage.
        api_response = api_instance.api_v1_report_get(include_app_usage=include_app_usage, include_team_members=include_team_members, team_members=team_members, start_date_min=start_date_min, start_date_max=start_date_max, projects=projects, include_child_projects=include_child_projects, search_query=search_query, columns=columns, project_grouping_level=project_grouping_level, include_project_data=include_project_data, timespan_grouping_mode=timespan_grouping_mode, sort=sort, authorization=authorization, content_type=content_type, accept=accept)
        pprint(api_response)
    except timingapp.ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_app_usage** | **str**| Whether to include app usage in the report. If false, only time entries are returned. Default: &#x60;0&#x60; | [optional]
 **include_team_members** | **str**| If true, the response will also contain time entries that belong to other team members, provided the current user has permission to view them. Default: &#x60;0&#x60; | [optional]
 **team_members** | **str**| Restricts the query to data associated with the given user. Can be repeated to include time entries from several users. | [optional]
 **start_date_min** | **str**| Restricts the query to data whose start date is equal to or later than this parameter. | [optional]
 **start_date_max** | **str**| Restricts the query to data whose start date is equal to or earlier than this parameter. | [optional]
 **projects** | **str**| Restricts the query to data associated with the given project. Can be repeated to include time entries from several projects. If you would like to include time entries that are not assigned to any project, you can provide an empty string, i.e. &#x60;projects[]&#x3D;&#x60; | [optional]
 **include_child_projects** | **str**| If true, the response will also contain time entries that belong to any child projects of the ones provided in &#x60;projects[]&#x60;. Default: &#x60;0&#x60; | [optional]
 **search_query** | **str**| Restricts the query to time entries whose title and/or notes contain all words in this parameter. The search is case-insensitive but diacritic-sensitive. Note: this parameter can not be used when app usage is included. | [optional]
 **columns** | **str**| Which columns to show. The &#x60;user&#x60; column is ignored if &#x60;include_team_members&#x60; is false. Possible values: &#x60;project&#x60;, &#x60;title&#x60;, &#x60;notes&#x60;, &#x60;timespan&#x60;, &#x60;user&#x60;. Default: &#x60;user&#x60;, &#x60;project&#x60;, &#x60;title&#x60;. &#x60;start_date&#x60; and &#x60;end_date&#x60; is shown when &#x60;timespan&#x60; column is sent. | [optional]
 **project_grouping_level** | **int**| When this argument is provided, report lines for projects below the given level will be aggregated by their parent project on the given level. For example, when &#x60;project_grouping_level&#x60; is 0, all times in sub-projects will be counted towards the corresponding project on the \&quot;root\&quot; (i.e. highest) level in the project tree. Can be a non-negative integer or -1. The default is -1, which indicates no grouping (i.e. all projects will be returned, regardless of how deep they are in the hierarchy). Requires &#x60;columns[]&#x60; to contain &#x60;project&#x60;. | [optional]
 **include_project_data** | **str**| If true, the properties of each line&#39;s project will be included in the response. Requires &#x60;columns[]&#x60; to contain &#x60;project&#x60;. | [optional]
 **timespan_grouping_mode** | **str**| When this argument is provided, report lines will be aggregated according to the given calendar unit. Possible values: &#x60;exact&#x60;, &#x60;day&#x60;, &#x60;week&#x60;, &#x60;month&#x60;, &#x60;year&#x60;. Default: &#x60;exact&#x60; | [optional]
 **sort** | **str**| Sort the results by the given column. Prepend column name with a dash (&#x60;-&#x60;) to sort descending. Default: &#x60;-duration&#x60;. Examples: &#x60;sort[]&#x3D;-duration&#x60; -&gt; Sort descending by duration. &#x60;sort[]&#x3D;user&amp;sort[]&#x3D;-duration&#x60; -&gt; Sort ascending by user, then descending by duration. | [optional]
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **accept** | **str**|  | [optional]

### Return type

[**ApiV1ReportGet200Response**](ApiV1ReportGet200Response.md)

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

