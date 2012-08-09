import os
from plugins.interface import Interface
from plugins.cpu import CPU
from plugins.mysql_connections import MysqlConnections

data_dir = "/var/lib/collectd/rrd/"
graphs_dir = "/var/www/graphs/"

for machine in os.listdir(data_dir):
	i = Interface(
		os.path.join(data_dir, machine),
		os.path.join(graphs_dir, machine),
	)
	cpu = CPU(
		os.path.join(data_dir, machine),
		os.path.join(graphs_dir, machine),
	)
	if machine == "mysql":
		mysql_connections = MysqlConnections(
			os.path.join(data_dir, machine),
			os.path.join(graphs_dir, machine),
		)
