from app import app

@app.task
def add(x, y):
    print x + y
