import os
import re
from plugin import MetaPlugin

class CPU(MetaPlugin):
    def gen(self):
        for filename in os.listdir(self._data_dir):
            if re.match("cpu-[0-9]{1,3}", filename):
                self.plugin_directory = filename
                self.name = filename
                self.graph_meta(self.name + "-%s.png")

    def graph_meta(self, *args):
        values = (
            #('idle', 'ffffff', 'cpu-idle.rrd'),
            ('nice', '00e000', 'cpu-nice.rrd'),
            ('user', '0000ff', 'cpu-user.rrd'),
            ('wait', 'ffb000', 'cpu-wait.rrd'),
            ('system', 'ff0000', 'cpu-system.rrd'),
            ('softirq', 'ff00ff', 'cpu-softirq.rrd'),
            ('interrupt', 'a000a0', 'cpu-interrupt.rrd'),
            ('steal', '000000', 'cpu-steal.rrd'),
        )
        return super(CPU, self).graph_meta(values, *args)
