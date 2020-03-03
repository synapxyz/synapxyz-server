from sanic.response import json
from sanic import Blueprint
from celery.result import GroupResult, AsyncResult
from synapxyz.utils.celery import make_celery
from synapxyz.connections.tasks import new_connection 
import celery_pubsub


connections = Blueprint('connections', url_prefix='connections')


@connections.route('/')
async def list_connections(request):
  res = celery_pubsub.publish('connections.new.init_test', data='something', value=42)
  res.get()
  res.save(res.backend)
  return json({'connections': res.as_tuple()})


@connections.route('/status/<task_id:string>')
async def get_result(request, task_id):
  app = make_celery()
  print('app')
  res = AsyncResult(task_id, app=app)
  print(res)
  return json({'result': res.status, 'id': task_id})
  
