from bottle import route, run, template, static_file, TEMPLATE_PATH
from main import gen_graphs, config
import sys

from os.path import join, abspath, pardir, dirname
ROOT = abspath(join(dirname(__file__), pardir, "collectd_graphs", "views"))
TEMPLATE_PATH.append(ROOT)

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