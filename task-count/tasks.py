from celery.task import task
from celery import Celery
from celery.task import Task
from celery.signals import after_task_publish, task_success
import json

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task(queue='trigger')
def trigger():
    print "show lists list worked...."  
    Counter.delay()
       
class Counter(Task):
    queue = "qcounter"  
    
    taskCount = 0;
    def __call__(self, *args, **kwargs):
        """In celery task this function call the run method, here you can
        set some environment variable before the run of the task"""
        print "haiiiii"
        Counter.taskCount += 1
        print Counter.taskCount
        return self.run(*args, **kwargs)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        #exit point of the task whatever is the state
        pass

    def run(self, *args, **kwargs):
        print "inside run****************"
        if Counter.taskCount == 5 :
           print "data base is updated"
           Counter.taskCount = 0 
        else :
           print "yet to go" 


   
