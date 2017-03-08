'''from __future__ import absolute_import, unicode_literals
from celery import Celery
import celeryconfig
 
app = Celery('proj',
             broker='amqp://',
             backend='amqp://',
             include=['proj.tasks_main','proj.tasks_sub'])

app.config_from_object('celeryconfig')
if __name__ == '__main__':
    app.start()
'''
from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('proj',
             broker='amqp://',
             backend='amqp://',
             include=['proj.tasks','proj.tasks_sub'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
