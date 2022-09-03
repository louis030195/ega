# ApiV1ProjectsGetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The project&#39;s title. | 
**parent** | [**Project**](Project.md) | A reference to an existing project. The new project will be appended to the parent&#39;s children. Can be a project reference in the form &#x60;\&quot;/projects/1\&quot;&#x60;, a project title (e.g. &#x60;\&quot;Project at root level\&quot;&#x60;), or an array with the project&#39;s entire title chain (e.g. &#x60;[\&quot;Project at root level\&quot;, \&quot;Unproductive child project\&quot;]&#x60;). | [optional] 
**color** | [**Color**](Color.md) | The project&#39;s color, in hexadecimal format (&#x60;#RRGGBB&#x60;). If omitted, a color with random hue, 70% saturation and 100% value will be used. | [optional] 
**productivity_score** | **float** | The project&#39;s productivity rating, between -1 (very unproductive) and 1 (very productive). Defaults to 1. | [optional] 
**is_archived** | **bool** | Whether the project has been archived. Defaults to false. | [optional] 
**team_id** | **int** | The ID of the team to add the project to. See [Return a list containing all the teams you are a member of.](#return-a-list-containing-all-the-teams-you-are-a-member-of) for obtaining a team ID to provide here. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


