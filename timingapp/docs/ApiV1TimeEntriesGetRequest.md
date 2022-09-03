# ApiV1TimeEntriesGetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | The time entry&#39;s start date and time. | 
**end_date** | **date** | The time entry&#39;s end date and time. | 
**project** | [**Project**](Project.md) | The project this time entry is associated with. Can be a project reference in the form &#x60;\&quot;/projects/1\&quot;&#x60;, a project title (e.g. &#x60;\&quot;Project at root level\&quot;&#x60;), or an array with the project&#39;s entire title chain (e.g. &#x60;[\&quot;Project at root level\&quot;, \&quot;Unproductive child project\&quot;]&#x60;). | [optional] 
**title** | **str** | The time entry&#39;s title. | [optional] 
**notes** | **str** | The time entry&#39;s notes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


