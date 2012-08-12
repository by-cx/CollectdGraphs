import os
from plugin import Plugin

class Df(Plugin):
    plugin_directory = "df"
    dst_name = "df"

    def gen(self):
        for filename in os.listdir(os.path.join(self._data_dir, self.plugin_directory)):
            self.graph_df(filename ,filename[:-4] + "-%s.png")
        
    def graph_df(self, *args):
        parms = [
                '-v', 'Percent', '-l', '0',
                'DEF:free_avg={file}:free:AVERAGE',
                'DEF:free_min={file}:free:MIN',
                'DEF:free_max={file}:free:MAX',
                'DEF:used_avg={file}:used:AVERAGE',
                'DEF:used_min={file}:used:MIN',
                'DEF:used_max={file}:used:MAX',
                'CDEF:total=free_avg,used_avg,+',
                'CDEF:free_pct=100,free_avg,*,total,/',
                'CDEF:used_pct=100,used_avg,*,total,/',
                'CDEF:free_acc=free_pct,used_pct,+',
                'CDEF:used_acc=used_pct',
                "AREA:free_acc#$HalfGreen",
                "AREA:used_acc#$HalfRed",
                "LINE1:free_acc#$FullGreen:Free",
                'GPRINT:free_min:MIN:%5.1lf%sB Min,',
                'GPRINT:free_avg:AVERAGE:%5.1lf%sB Avg,',
                'GPRINT:free_max:MAX:%5.1lf%sB Max,',
                'GPRINT:free_avg:LAST:%5.1lf%sB Last\l',
                "LINE1:used_acc#$FullRed:Used",
                'GPRINT:used_min:MIN:%5.1lf%sB Min,',
                'GPRINT:used_avg:AVERAGE:%5.1lf%sB Avg,',
                'GPRINT:used_max:MAX:%5.1lf%sB Max,',
                'GPRINT:used_avg:LAST:%5.1lf%sB Last\l',
        ]
        self.gen_graph(parms, *args)