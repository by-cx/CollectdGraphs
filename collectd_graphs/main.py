import os
import json
import plugins
import re

config = {
    "data_dir": "/var/lib/collectd/rrd/",
    "graphs_dir": "/var/www/graphs/",
}

config_for_update = {}
if os.path.isfile("/etc/collectd/graphs.json"):
    with open("/etc/collectd/graphs.json") as f:
        config_for_update = json.load(f)
if config_for_update:
    config.update(config_for_update)
# Ugly hack for rrdtool
for cfg in config: config[cfg] = str(config[cfg])


def gen_graphs(plugin=""):
    data = {}
    for machine in os.listdir(config["data_dir"]):
        data[machine] = {}
        for Plugin in plugins.plugins_list:
            data[machine][Plugin.dst_name] = {"day": [], "week": [], "month": [], "three-months": [], "six-months": [], "year": []}
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