import os
from plugin import Plugin

class MysqlConnections(Plugin):
    plugin_directory = "dbi-lotofideasql"
    dst_name = "dbi-lotofideasql"

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
            'LINE1:connections_max#$FullRed:Connections Max',
            'AREA:connections_avg#$HalfYellow:Connections Avg',
            'LINE1:connections_min#$FullBlue:Connections Min',
            'GPRINT:connections_avg:MIN:Connections %5.1lf%s Min ',
            'GPRINT:connections_max:AVERAGE:%5.1lf%s Avg ',
            'GPRINT:connections_avg:MAX:%5.1lf%s Max\l',
        ]
        self.gen_graph(parms, *args)
        