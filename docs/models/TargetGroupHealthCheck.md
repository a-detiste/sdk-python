# TargetGroupHealthCheck

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **check_timeout** | **int** | The maximum time in milliseconds to wait for a target to respond to a check. For target VMs with &#39;Check Interval&#39; set, the lesser of the two  values is used once the TCP connection is established. | [optional]  |
| **check_interval** | **int** | The interval in milliseconds between consecutive health checks; default is 2000. | [optional]  |
| **retries** | **int** | The maximum number of attempts to reconnect to a target after a connection failure. Valid range is 0 to 65535, and default is three reconnection attempts. | [optional]  |


