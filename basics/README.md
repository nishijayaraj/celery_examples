For this to works, when we invoke a worker with the command :-  celery worker -A proj -l info, we should keep a module named celery.py with from __future__ import absolute_import   
This is to diffrentiate the core celery module from the user defined celery module. 
If we are using other name for module that defines celery app, it should be like 

celery worker -A proj.app (here app.py)

Steps to Run this Program
=========================
* CD to the parent folder which contains the folder proj
* Then type the command  in terminal :
     celery worker -A proj -l

This will now list worker with details including assocaited tasks names,


Now open another terminal from same location,
 Open a python interpreter using python
 Then Type in
        from proj.tasks_sub import mul
        mul.delay(1,6)
Now check in the terminal of worker, You would be able to see the result.
