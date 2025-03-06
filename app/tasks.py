from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)
