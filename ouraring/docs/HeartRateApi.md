# ouraring.HeartRateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heartrate_route_heartrate_get**](HeartRateApi.md#heartrate_route_heartrate_get) | **GET** /v2/usercollection/heartrate | Get Heart Rate


# **heartrate_route_heartrate_get**
> HeartRateResponse heartrate_route_heartrate_get()

Get Heart Rate

Returns available heart rate data for a specified Oura user within a given timeframe

### Example


```python
import time
import ouraring
from ouraring.api import heart_rate_api
from ouraring.model.error import Error
from ouraring.model.heart_rate_response import HeartRateResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ouraring.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ouraring.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = heart_rate_api.HeartRateApi(api_client)
    start_datetime = "start_datetime_example" # str |  (optional)
    end_datetime = "end_datetime_example" # str |  (optional)
    next_token = "next_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Heart Rate
        api_response = api_instance.heartrate_route_heartrate_get(start_datetime=start_datetime, end_datetime=end_datetime, next_token=next_token)
        pprint(api_response)
    except ouraring.ApiException as e:
        print("Exception when calling HeartRateApi->heartrate_route_heartrate_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_datetime** | **str**|  | [optional]
 **end_datetime** | **str**|  | [optional]
 **next_token** | **str**|  | [optional]

### Return type

[**HeartRateResponse**](HeartRateResponse.md)

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

