celery worker --loglevel=INFO --concurrency=1 -n worker1.%h

/** count worker should contain one worker only in its pool **/

 celery worker --loglevel=INFO -Q counter --concurrency=1 -n worker1.%h

celery worker -Q letter -n worker2.%h




celery worker -Q qcounter -l info -A tasks -C 1
 celery worker -Q trigger -l info -A tasks
****************************************************************************************************

Deleting all pending tasks in celery/rabbitMQ
From the docs:

$ celeryctl purge
or

from celery.task.control import discard_all
discard_all()
