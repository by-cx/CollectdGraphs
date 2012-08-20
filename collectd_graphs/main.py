import os
import json
import plugins
import re

config = {
    "data_dir": "/var/lib/collectd/rrd/",
    "graphs_dir": "/var/www/graphs/",
    "conf_path": "/var/lib/collectd_graphs/conf.json",
}

config_for_update = {}
if os.path.isfile("/etc/collectd/graphs.json"):
    with open("/etc/collectd/graphs.json") as f:
        config_for_update = json.load(f)
if config_for_update:
    config.update(config_for_update)
# Ugly hack for rrdtool
for cfg in config: config[cfg] = str(config[cfg])

if not os.path.isdir(config["graphs_dir"]):
    os.makedirs(config["graphs_dir"])

class JSONConf(object):
    def __init__(self, path):
        self.path = path
        self.data = None
        self._load()

    def _load(self):
        with open(self.path) as f:
            self.data = json.load(f)

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f)

    def get(self, name):
        return self.data.get(name)

    def set(self, name, value):
        self.data[name] = value
        self._save()


def get_plugins_list():
    data = {}
    for machine in os.listdir(config["graphs_dir"]):
        data[machine] = []
        for plugin in os.listdir(os.path.join(config["graphs_dir"], machine)):
            data[machine].append(plugin)
    return data

def tmp_graph(machine, plugin_name, x, y, filename):
    for Plugin in plugins.plugins_list:
        if Plugin.dst_name == plugin_name:
            plugin = Plugin(
                os.path.join(config["data_dir"], machine),
                os.path.join(config["graphs_dir"], machine),
                (x, y),
                True
            )
            plugin.gen()
            return plugin.images[filename]

def gen_graphs(fmachine="", fplugin=""):
    data = {}
    for machine in os.listdir(config["data_dir"]):
        if fmachine and fmachine != machine: continue
        data[machine] = {}
        for Plugin in plugins.plugins_list:
            if fplugin and fplugin != Plugin.dst_name: continue
            if not Plugin.dst_name in data[machine]: data[machine][Plugin.dst_name] = {"day": [], "week": [], "month": [], "three-months": [], "six-months": [], "year": []}
            for path in os.listdir(os.path.join(config["data_dir"], machine)):
                if re.match("^%s$" % Plugin.plugin_directory, path):
                    plugin = Plugin(
                        os.path.join(config["data_dir"], machine),
                        os.path.join(config["graphs_dir"], machine),
                    )
                    plugin.gen()
                    if plugin.graphs:
                        for filename in plugin.graphs:
                            for time in data[machine][Plugin.dst_name]:
                                if re.search("-%s.png$" % time, filename):
                                    data[machine][Plugin.dst_name][time].append(filename)
                                    break
                    break
    return data

if __name__ == "__main__":
    gen_graphs()
