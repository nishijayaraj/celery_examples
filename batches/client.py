from celery import Celery
#import tasks ---> importing tasks.py is alternative to including  the same in celery app instance

results = []
#app = Celery('demo', broker='amqp://guest@localhost//')
#the first arg should be the name of the current module in which( here "client.py") celery app is defined 
app = Celery('client',
         broker='amqp://guest@localhost//',
         backend='amqp://',
         include=['tasks'])
#celery.config_from_object('celeryconfig')
print app
print __name__
if __name__ =="__main__" :
	app.start()

'''

If there is any import related issues for this task.py it may lead to task unrgistered error '''
