import rrdtool

path = "/var/lib/collectd/rrd/mysql/dbi-lotofideasql/gauge-customer-connections.rrd"

parms = [
    '--imgformat', 'PNG',
    '--width', '540',
    '--height', '100',
    '--start', "-%s" % "1d",
    '--end', "-1",
    '--vertical-label', 'MySQL',
    '--title', 'Connections to MySQL',
    '--lower-limit', '0',    
    'DEF:connections_max=%s:value:MAX' % path,
    'DEF:connections_avg=%s:value:AVERAGE' % path,
    'DEF:connections_min=%s:value:MIN' % path,
    #'AREA:connections_min#110033:Connections min',
    #'AREA:connections_avg#550033:Connections avg',
    'AREA:connections_max#990033:Connections max',
]

rrdtool.graph('/var/www/graphs/mysql_connections.png', parms)
