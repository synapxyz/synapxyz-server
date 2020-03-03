import celery_pubsub
from synapxyz.utils.celery import make_celery

celery = make_celery()

@celery.task
def new_connection(*args, **kwargs):
  print('new connection')  
  return "new connection created"


def register_tasks():
  celery_pubsub.subscribe('connections.new.*', new_connection)
