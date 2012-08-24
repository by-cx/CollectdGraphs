from plugin import Plugin

class Conntrack(Plugin):
    plugin_directory = "conntrack"
    dst_name = "conntrack"

    def gen(self):
        self.gen_graph("%s.rrd" % self.plugin_directory, self.plugin_directory + "-%s.png")

    def gen_graph(self, *args):
        parms = [
            '-v', 'Conntrack',
            'DEF:entries_avg={file}:entropy:AVERAGE',
            'DEF:entries_min={file}:entropy:MIN',
            'DEF:entries_max={file}:entropy:MAX',
            "AREA:entries_max#$HalfRed",
            "AREA:entries_min#$Canvas",
            "LINE1:entries_avg#$FullGreen: Entries",
            'GPRINT:entries_min:MIN:%4.2lf Min,',
            'GPRINT:entries_avg:AVERAGE:%4.2lf Avg,',
            'GPRINT:entries_max:MAX:%4.2lf Max,',
            'GPRINT:entries_avg:LAST:%4.2lf Last',
        ]
        super(Conntrack, self).gen_graph(parms, *args)
