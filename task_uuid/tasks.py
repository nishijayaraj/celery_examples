from celery import Celery


app = Celery('tasks')
app.config_from_object('celeryconfig')
 
'''@app.task()
def get_ID(task_id=None):
   print "hiiiiii" 
   print task_id'''
 
@app.task(bind=True,name="tasks.get_ID")
def get_ID(self):
   print "hooo" 
   print self.request.id
 
   
