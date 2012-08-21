import re
import os
from plugin import Plugin

class IRQ(Plugin):
    plugin_directory = "irq"
    dst_name = "irq"

    def gen(self):
        for filename in os.listdir(self.data_dir):
            if re.match("irq-[0-9]{1,6}.rrd", filename):
                self.graph(filename, filename.replace(".rrd", "-%s.png"))

    def graph(self, *args):
        parms = [
            '-v', 'Issues/s',
            'DEF:avg={file}:value:AVERAGE',
            'DEF:min={file}:value:MIN',
            'DEF:max={file}:value:MAX',
            'AREA:max#$HalfBlue',
            'AREA:min#$Canvas',
            'LINE1:avg#$FullBlue:Issues/s',
            'GPRINT:min:MIN:%6.2lf Min,',
            'GPRINT:avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:max:MAX:%6.2lf Max,',
            'GPRINT:avg:LAST:%6.2lf Last\l',
        ]
        self.gen_graph(parms, *args)
