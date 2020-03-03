from sanic import Sanic
from synapxyz.connections.views import connections
from synapxyz.connections.tasks import register_tasks

app = Sanic(__name__)
app.blueprint(connections)

register_tasks()

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=9090, debug=True)
