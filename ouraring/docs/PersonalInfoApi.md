# ouraring.PersonalInfoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**personal_info_route_get**](PersonalInfoApi.md#personal_info_route_get) | **GET** /v2/usercollection/personal_info | Get Personal Info


# **personal_info_route_get**
> PersonalInfoResponse personal_info_route_get()

Get Personal Info

Returns personal info data for the specified Oura user.

### Example


```python
import time
import ouraring
from ouraring.api import personal_info_api
from ouraring.model.personal_info_response import PersonalInfoResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ouraring.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ouraring.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = personal_info_api.PersonalInfoApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Personal Info
        api_response = api_instance.personal_info_route_get()
        pprint(api_response)
    except ouraring.ApiException as e:
        print("Exception when calling PersonalInfoApi->personal_info_route_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PersonalInfoResponse**](PersonalInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

