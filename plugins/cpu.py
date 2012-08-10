import os
import re
from plugin import MetaPlugin

class CPU(MetaPlugin):
    def gen(self):
        for filename in os.listdir(self._data_dir):
            if re.match("cpu-[0-9]{1,3}", filename):
                self.plugin_directory = filename
                self.name = "cpu"
                self.graph_meta(filename + "-%s.png")

    def graph_meta(self, *args):
        values = (
            #('idle', 'ffffff', '%s/cpu-idle.rrd' % self.plugin_directory),
            ('nice', '00e000', '%s/cpu-nice.rrd' % self.plugin_directory),
            ('user', '0000ff', '%s/cpu-user.rrd' % self.plugin_directory),
            ('wait', 'ffb000', '%s/cpu-wait.rrd' % self.plugin_directory),
            ('system', 'ff0000', '%s/cpu-system.rrd' % self.plugin_directory),
            ('softirq', 'ff00ff', '%s/cpu-softirq.rrd' % self.plugin_directory),
            ('interrupt', 'a000a0', '%s/cpu-interrupt.rrd' % self.plugin_directory),
            ('steal', '000000', '%s/cpu-steal.rrd' % self.plugin_directory),
        )
        return super(CPU, self).graph_meta(values, *args)
