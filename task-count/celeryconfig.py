CELERY_RESULT_BACKEND = "amqp"
BROKER_URL='amqp://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1

