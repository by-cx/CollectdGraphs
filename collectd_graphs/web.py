from bottle import route, run, template, static_file
from main import gen_graphs, config
import sys

@route('/')
def index(name=''):
    graphs = gen_graphs()
    return template('home', data=graphs)

@route("/static/<path:path>")
def callback(path):
    return static_file(path, root=config["graphs_dir"])

def main():
    #needs more love
    run(host=sys.argv[1].split(":")[0], port=sys.argv[1].split(":")[1])

if __name__ == "__main__":
    main()