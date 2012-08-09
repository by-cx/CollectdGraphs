import os
from plugins.interface import Interface
from plugins.cpu import CPU

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

<<<<<<< HEAD
data_dir = "/var/lib/collectd/rrd/"
graphs_dir = "/var/www/graphs/"

for machine in os.listdir(data_dir):
	i = Interface(
		os.path.join(data_dir, machine),
		os.path.join(graphs_dir, machine),
	)
=======
>>>>>>> df85fdb4e320c9d483b022f05c78defbded075e0
