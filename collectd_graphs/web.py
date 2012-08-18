from bottle import route, run, template, static_file, TEMPLATE_PATH, redirect, response

from main import gen_graphs, config, get_plugins_list, tmp_graph, JSONConf
import sys

from os.path import join, abspath, pardir, dirname
ROOT = abspath(join(dirname(__file__), pardir, "collectd_graphs", "views"))
TEMPLATE_PATH.append(ROOT)

#conf = JSONConf(config["conf_path"])

@route('/')
def index(name=''):
    graphs = get_plugins_list()
    return template('home', data=graphs)

# for example: http://localhost:8080/plugin_tmp/web/load/600/120/load-day.png
@route('/plugin_tmp/:machine/:plugin/:x/:y/:filename')
def plugin_tmp(machine, plugin, x, y, filename):
    response.content_type = "image/png"
    return tmp_graph(machine, plugin, int(x), int(y), filename)

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