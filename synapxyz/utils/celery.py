from celery import Celery
import celery
__celery = None


def make_celery():
    global __celery
    print(__celery)
    if not __celery:
      print('new celery')
      __celery = Celery('synapxyz', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0', include=['synapxyz.connections.tasks'])
      celery.app = __celery
      celery.current_app = __celery

    return __celery
