from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')


@app.task(name="tasks.add")
def add(x, y):
   # return x + y
   print "haiii"
   print x+y

@app.task(name="tasks.sub")
def sub():
    print "subtraction"
   


