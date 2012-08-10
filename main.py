import os
import json
from plugins.interface import Interface
from plugins.memory import Memory
from plugins.disk import Disk
from plugins.load import Load
from plugins.cpu import CPU
from plugins.mysql_connections import MysqlConnections

#data_dir = "/var/lib/collectd/rrd/"
#graphs_dir = "/var/www/graphs/"
data_dir = "/home/cx/point/var/lib/collectd/rrd/"
graphs_dir = "/home/cx/point/var/www/graphs/"

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

for machine in os.listdir(config["data_dir"]):
    Memory(
        os.path.join(config["data_dir"], machine),
        os.path.join(config["graphs_dir"], machine),
    )
    Load(
        os.path.join(config["data_dir"], machine),
        os.path.join(config["graphs_dir"], machine),
    )
    Interface(
        os.path.join(config["data_dir"], machine),
        os.path.join(config["graphs_dir"], machine),
    )
    cpu = CPU(
        os.path.join(config["data_dir"], machine),
        os.path.join(config["graphs_dir"], machine),
    )
    if machine == "mysql":
        mysql_connections = MysqlConnections(
            os.path.join(config["data_dir"], machine),
            os.path.join(config["graphs_dir"], machine),
        )
    Disk(
        os.path.join(config["data_dir"], machine),
        os.path.join(config["graphs_dir"], machine),
    )
