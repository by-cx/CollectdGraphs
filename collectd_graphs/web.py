from bottle import route, run, template, static_file, TEMPLATE_PATH, redirect

from main import gen_graphs, config, get_plugins_list
import sys

from os.path import join, abspath, pardir, dirname
ROOT = abspath(join(dirname(__file__), pardir, "collectd_graphs", "views"))
TEMPLATE_PATH.append(ROOT)

@route('/')
def index(name=''):
    graphs = get_plugins_list()
    return template('home', data=graphs)

@route('/plugin/:machine/:plugin/:time')
def plugin(machine, plugin, time):
    plugin_graphs = gen_graphs(machine, plugin)[machine][plugin][time]
    return template(
        'plugin',
        data=plugin_graphs,
        machine=machine,
        plugin=plugin,
        time=time,
    )

@route("/static/<path:path>")
def callback(path):
    return static_file(path, root=config["graphs_dir"])

@route('/all')
def gen_all():
    gen_graphs()
    redirect("/", 307)

def main():
    #needs more love
    run(host=sys.argv[1].split(":")[0], port=sys.argv[1].split(":")[1])

if __name__ == "__main__":
    main()