from celery import Celery
import celery_pubsub
from synapxyz.utils.celery import make_celery
import synapxyz.connections.tasks

app = make_celery() 
