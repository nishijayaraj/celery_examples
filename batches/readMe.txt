celery Batch guarantees a bulk execution of messages,
This can be done based  either on message number or time interval or on both
the attribute flush_every specifies the number of messages, on reaching which the task would be executed

flush_interval
The attribute  specifies the time, on reaching which the task would be executed
The default value is 10 seconds.

If both of these attributes are specified, the tasks will be executed in bulk whenever reaches its stated length of messages and also the stated time period.

If we need to execute the bulk messages only on the number of task basis, we need to explicitly set flust_interval = 0. If nothing is specified it will take a0 sec as default value.
