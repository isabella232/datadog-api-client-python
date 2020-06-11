# logs_list_request.LogsListRequest

Object to send with the request to retrieve a list of logs from your Organization.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The search query - following the log search syntax. | 
**time** | [**logs_list_request_time.LogsListRequestTime**](LogsListRequestTime.md) |  | 
**index** | **str** | For multi-index organizations, the log index in which the request is performed. | [optional] 
**limit** | **int** | Number of logs return in the response. | [optional] 
**sort** | [**logs_sort.LogsSort**](LogsSort.md) |  | [optional] 
**start_at** | **str** | Hash identifier of the first log to return in the list, available in a log &#x60;id&#x60; attribute. This parameter is used for the pagination feature.  **Note**: This parameter is ignored if the corresponding log is out of the scope of the specified time window. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

