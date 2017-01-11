Enter the working directory task-callback:
Then run the following command to start the project :
celery worker -A tasks -l info

Then generate invoke the tasks :
From the above directory open a python interpreter and type the following :

python : To start a python interpreter :
Then tasks invocation :
add.apply_async((2, 2), link=sub.si())

This would call the task sub if the add tasks has been successfully executed.
