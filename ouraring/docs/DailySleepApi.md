# ouraring.DailySleepApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**daily_sleep_route_daily_sleep_get**](DailySleepApi.md#daily_sleep_route_daily_sleep_get) | **GET** /v2/usercollection/daily_sleep | Get Daily Sleep


# **daily_sleep_route_daily_sleep_get**
> DailySleep daily_sleep_route_daily_sleep_get()

Get Daily Sleep

Returns Oura Daily Sleep data for the specified Oura user within a given timeframe

### Example


```python
import time
import ouraring
from ouraring.api import daily_sleep_api
from ouraring.model.error import Error
from ouraring.model.daily_sleep import DailySleep
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ouraring.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ouraring.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = daily_sleep_api.DailySleepApi(api_client)
    start_date = dateutil_parser('1970-01-01').date() # date |  (optional)
    end_date = dateutil_parser('1970-01-01').date() # date |  (optional)
    next_token = "next_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Daily Sleep
        api_response = api_instance.daily_sleep_route_daily_sleep_get(start_date=start_date, end_date=end_date, next_token=next_token)
        pprint(api_response)
    except ouraring.ApiException as e:
        print("Exception when calling DailySleepApi->daily_sleep_route_daily_sleep_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | [optional]
 **end_date** | **date**|  | [optional]
 **next_token** | **str**|  | [optional]

### Return type

[**DailySleep**](DailySleep.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Query Parameter Validation Error |  -  |
**426** | Minimum App Version Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

