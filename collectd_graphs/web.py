from bottle import route, run, template, static_file, TEMPLATE_PATH, redirect, response, request

from main import gen_graphs, config, get_plugins_list, tmp_graph, JSONConf
import sys

from os.path import join, abspath, pardir, dirname
ROOT_TMPL = abspath(join(dirname(__file__), pardir, "collectd_graphs", "views"))
TEMPLATE_PATH.append(ROOT_TMPL)
ROOT_STATIC = abspath(join(dirname(__file__), pardir, "collectd_graphs", "static"))

conf = JSONConf(config["conf_path"])

@route('/key/set')
def set_key():
    key = request.forms.get('key')
    value = request.forms.get('value')
    conf.set(key, value)
    return {"status": "ok"}

@route('/key/get')
def get_key(key, default=None):
    key = request.forms.get('key')
    return {"status": "ok", "data": conf.get(key, default)}

@route('/')
def index(name=''):
    graphs = get_plugins_list()
    comparators = conf.get("comparators", {})
    return template('home', data=graphs, comparators=comparators)

@route('/comparator/show/:comparator')
def comparator(comparator):
    comparators = conf.get("comparators", {})
    return template('comparator', comparator=comparator, graphs=comparators[comparator])

@route('/comparator/delete/:comparator/:machine/:plugin/:time/:graph')
def delete_from_comparator(comparator, machine, plugin, time, graph):
    comparators = conf.get("comparators", {})
    if comparator in comparators:
        comparators[comparator].remove([machine, plugin, time, graph])
        if not comparators[comparator]:
            comparators.pop(comparator)
            redirect("/", 307)
        redirect("/comparator/show/%s" % comparator, 307)
        conf.set("comparators", comparators)
        return "ok"
    return "Error: comparator doesn't exists"

@route('/comparator/add/:comparator/:machine/:plugin/:time/:graph')
def add_to_comparator(comparator, machine, plugin, time, graph):
    comparators = conf.get("comparators", {})
    if comparator in comparators and (machine, plugin, time, graph) not in comparators[comparator]:
        comparators[comparator].append((machine, plugin, time, graph))
    else:
        comparators[comparator] = [(machine, plugin, time, graph)]
    conf.set("comparators", comparators)
    return "ok"

@route('/comparator/choose/:machine/:plugin/:time/:graph')
def choose_comparator(machine, plugin, time, graph):
    comparators = conf.get("comparators", [])
    return template(
        'comparator_chooser',
        comparators = comparators,
        machine = machine,
        plugin = plugin,
        time = time,
        graph = graph,
    )

# for example: http://localhost:8080/plugin_tmp/web/load/600/120/load-day.png
@route('/plugin_tmp/:machine/:plugin/:x/:y/:filename')
def plugin_tmp(machine, plugin, x, y, filename):
    response.content_type = "image/png"
    return tmp_graph(machine, plugin, int(x), int(y), filename)

@route('/plugin/:machine/:plugin/:time')
def plugin(machine, plugin, time):
    time_ranges = ("day", "week", "month", "three-months", "six-months", "year")
    if time and time not in time_ranges:
        selected_time = "custom"
    elif time and time in time_ranges:
        selected_time = time
    else:
        selected_time = "day"
    plugin_graphs = gen_graphs(machine, plugin, time)[machine][plugin][selected_time]
    graphs = get_plugins_list()
    return template(
        'plugin',
        data=plugin_graphs,
        machine=machine,
        plugin=plugin,
        time=time,
        plugins=graphs[machine],
    )

@route("/static/<path:path>")
def get_file(path):
    return static_file(path, root=ROOT_STATIC)

@route("/graph/<path:path>")
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
