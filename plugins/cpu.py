import os
import re
from plugin import MetaPlugin

class CPU(MetaPlugin):
    def gen(self):
        for filename in os.listdir(self._data_dir):
            if re.match("cpu-[0-9]{1,3}", filename):
                self.plugin_directory = filename
                self.dst_name = "cpu"
                self.graph_meta(filename + "-%s.png")

    def graph_meta(self, *args):
        values = (
            ('nice', '00e000', 'cpu-nice.rrd', "value"),
            ('user', '0000ff', 'cpu-user.rrd', "value"),
            ('wait', 'ffb000', 'cpu-wait.rrd', "value"),
            ('system', 'ff0000', 'cpu-system.rrd', "value"),
            ('softirq', 'ff00ff', 'cpu-softirq.rrd', "value"),
            ('interrupt', 'a000a0', 'cpu-interrupt.rrd', "value"),
            ('steal', '000000', 'cpu-steal.rrd', "value"),
            #('idle', 'ffffff', 'cpu-idle.rrd', "value"),
        )
        return super(CPU, self).graph_meta(values, *args)
