import os
from plugins.interface import Interface

data_dir = "/var/lib/collectd/rrd/"
graphs_dir = "/var/www/graphs/"

for machine in os.listdir(data_dir):
	i = Interface(
		os.path.join(data_dir, machine),
		os.path.join(graphs_dir, machine),
	)
