# DailyActivityModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_calories** | **int** | Active calories expended (in kilocalories) | 
**average_met_minutes** | **float** | Average metabolic equivalent (MET) in minutes | 
**contributors** | [**ActivityContributors**](ActivityContributors.md) |  | 
**equivalent_walking_distance** | **int** | Equivalent walking distance (in meters) of energy expenditure | 
**high_activity_met_minutes** | **int** | High activity metabolic equivalent (MET) in minutes | 
**high_activity_time** | **int** | High activity metabolic equivalent (MET) in seconds | 
**inactivity_alerts** | **int** | Number of inactivity alerts received | 
**low_activity_met_minutes** | **int** | Low activity metabolic equivalent (MET) in minutes | 
**low_activity_time** | **int** | Low activity metabolic equivalent (MET) in seconds | 
**medium_activity_met_minutes** | **int** | Medium activity metabolic equivalent (MET) in minutes | 
**medium_activity_time** | **int** | Medium activity metabolic equivalent (MET) in seconds | 
**met** | [**METSample**](METSample.md) |  | 
**meters_to_target** | **int** | Remaining meters to target (from &#x60;&#x60;&#x60;target_meters&#x60;&#x60;&#x60;) | 
**non_wear_time** | **int** | The time (in seconds) in which the ring was not worn | 
**resting_time** | **int** | Resting time (in seconds) | 
**sedentary_met_minutes** | **int** | Sedentary metabolic equivalent (MET) in minutes | 
**sedentary_time** | **int** | Sedentary metabolic equivalent (MET) in seconds | 
**steps** | **int** | Total number of steps taken | 
**target_calories** | **int** | Daily activity target (in kilocalories) | 
**target_meters** | **int** | Daily activity target (in meters) | 
**total_calories** | **int** | Total calories expended (in kilocalories)  | 
**day** | **date** | The &#x60;&#x60;&#x60;YYYY-MM-DD&#x60;&#x60;&#x60; formatted local date indicating when the daily activity occurred | 
**timestamp** | **str** | ISO 8601 formatted local timestamp indicating the start datetime of when the daily activity occurred | 
**class_5_min** | **str** | 5-minute activity classification for the activity period: * &#x60;&#x60;&#x60;0&#x60;&#x60;&#x60; non wear * &#x60;&#x60;&#x60;1&#x60;&#x60;&#x60; rest * &#x60;&#x60;&#x60;2&#x60;&#x60;&#x60; inactive * &#x60;&#x60;&#x60;3&#x60;&#x60;&#x60; low activity * &#x60;&#x60;&#x60;4&#x60;&#x60;&#x60; medium activity * &#x60;&#x60;&#x60;5&#x60;&#x60;&#x60; high activity | [optional] 
**score** | **int** | Activity score in range &#x60;&#x60;&#x60;[1, 100]&#x60;&#x60;&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


