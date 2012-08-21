from plugin import Plugin

class IRQ(Plugin):
    plugin_directory = "irq"
    dst_name = "irq"

    def gen(self):
        self.graph("irq.rrd", self.dst_name + "-%s.png")

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
