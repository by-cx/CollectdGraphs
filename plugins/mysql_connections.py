import os
from plugin import Plugin

class MysqlConnections(Plugin):
    plugin_directory = "dbi-lotofideasql"

    def __init__(self, *args, **kwargs):
        super(MysqlConnections, self).__init__(*args, **kwargs)
        self.gen()

    def gen(self):
        source = "gauge-customer-connections.rrd"
        dst = "mysql-connections-%s.png"
        self.graph(source, dst)

    def graph(self, *args):
        parms = [
            '-v', 'Connections', '--units=si',
            'DEF:connections_max={file}:value:MAX',
            'DEF:connections_avg={file}:value:AVERAGE',
            'DEF:connections_min={file}:value:MIN',
            'LINE1:connection_max#$FullRed:Connections Max',
            'AREA:connections_avg#$HalfYellow:Connections Avg',
            'LINE1:connection_min#$FullBlue:Connections Min',
        ]
        self.gen_graph(parms, *args)
        