import os
import re
from plugin import Plugin

class CPU(Plugin):
    plugin_directory = "cpu-x"

    def __init__(self, *args, **kwargs):
        """
            CPU graph plugin
            
            cpunum - number of CPU
        """
        super(CPU, self).__init__(*args, **kwargs)

        self.gen()

    def gen(self):
        for filename in os.listdir(self._data_dir):
            if re.match("cpu-[0-9]{1,3}", filename):
                self.plugin_directory = filename
                self.graph_meta("", self.plugin_directory + "-%s.png")

    def graph_meta(self, *args):
        values = (
            #('idle', 'ffffff', 'cpu-idle.rrd'),
            ('nice', '00e000', 'cpu-nice.rrd'),
            ('user', '0000ff', 'cpu-user.rrd'),
            ('wait', 'ffb000', 'cpu-wait.rrd'),
            ('system', 'ff0000', 'cpu-system.rrd'),
            ('softirq', 'ff00ff', 'cpu-softirq.rrd'),
            ('interrupt', 'a000a0', 'cpu-interrupt.rrd'),
            #('steal', '000000', 'cpu-steal.rrd'),
        )
        parms = []

        for name, color, rrd in values:
            parms.append('DEF:%s_min=%s:value:AVERAGE' % (name, os.path.join(self.data_dir, rrd)))
            parms.append('DEF:%s_avg=%s:value:AVERAGE' % (name, os.path.join(self.data_dir, rrd)))
            parms.append('DEF:%s_max=%s:value:AVERAGE' % (name, os.path.join(self.data_dir, rrd)))

        last_value = ""
        for name, color, rrd in values:
            if last_value:
                parms.append('CDEF:%s_up=%s_avg,%s_up,+' % (name, name, last_value))
            else:
                parms.append('CDEF:%s_up=%s_avg' % (name, name))
            last_value = name
        if last_value:
            parms.append("LINE1:%s_up#$FullGreen:Load" % last_value)
        for name, color, rrd in values:
            parms.append("AREA:%s_up#%s" % (name, color))
        for name, color, rrd in values:
            parms.append('GPRINT:{name}_avg:MIN:{name} %5.1lf%s Min,'.replace('{name}', name))
            parms.append('GPRINT:{name}_max:AVERAGE:%5.1lf%s Avg,'.replace('{name}', name))
            parms.append('GPRINT:{name}_avg:MAX:%5.1lf%s Max\l'.replace('{name}', name))
        self.gen_graph(parms, *args)
        
