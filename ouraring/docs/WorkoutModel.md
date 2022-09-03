# WorkoutModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **str** | The workout activity type | 
**day** | **date** | The &#x60;&#x60;&#x60;YYYY-MM-DD&#x60;&#x60;&#x60; formatted local date indicating when the workout was recorded | 
**end_datetime** | **str** | ISO 8601 formatted local timestamp indicating when the workout ended | 
**intensity** | **str** | The workout intensity: * &#x60;&#x60;&#x60;easy&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;moderate&#x60;&#x60;&#x60; * &#x60;&#x60;&#x60;hard&#x60;&#x60;&#x60; | 
**source** | **str** | The data source where the Workout data was collected from: * &#x60;&#x60;&#x60;manual&#x60;&#x60;&#x60; Workouts which were manually entered by the user * &#x60;&#x60;&#x60;autodetected&#x60;&#x60;&#x60; Workouts autodetected by Oura * &#x60;&#x60;&#x60;confirmed&#x60;&#x60;&#x60; Workouts autodetected by Oura and confirmed by the user * &#x60;&#x60;&#x60;workout_heart_rate&#x60;&#x60;&#x60; Workouts recorded with the Workout HR feature | 
**start_datetime** | **str** | ISO 8601 formatted local timestamp indicating when the workout started | 
**calories** | **float** | The number of calories (kcal) burned during the workout | [optional] 
**distance** | **float** | The distance (measured in meters) traveled during the workout | [optional] 
**label** | **str** | User-defined label for the workout | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


