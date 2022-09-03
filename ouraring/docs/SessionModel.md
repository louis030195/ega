# SessionModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **date** | The date when the session occurred | 
**start_datetime** | **str** | The start datetime when the session occurred | 
**end_datetime** | **str** | The end datetime when the session occurred | 
**type** | **str** | The session type: * &#x60;&#x60;&#x60;breathing&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;meditation&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;nap&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;relaxation&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;rest&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;body_status&#x60;&#x60;&#x60; | 
**heart_rate** | [**HRTSample**](HRTSample.md) |  | [optional] 
**heart_rate_variability** | [**HRVSample**](HRVSample.md) |  | [optional] 
**mood** | **str** | The user&#39;s selected mood after the session: * &#x60;&#x60;&#x60;bad&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;worse&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;same&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;good&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;great&#x60;&#x60;&#x60; | [optional] 
**motion_count** | [**Sample**](Sample.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


