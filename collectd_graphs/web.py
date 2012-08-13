from bottle import route, run, template, static_file
from main import gen_graphs, config

@route('/')
def index(name=''):
    graphs = gen_graphs()
    return template('home', data=graphs)

@route("/static/<path:path>")
def callback(path):
    return static_file(path, root=config["graphs_dir"])

run(host='localhost', port=8080)