
from app import app

@app.task
def mul(x, y):
    print x*y
