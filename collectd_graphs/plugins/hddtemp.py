from plugin import Plugin

class HDDTemp(Plugin):
    plugin_directory = "hddtemp"
    dst_name = "hddtemp"

    def gen(self):
        for splited, source, dst in self.scan_for_files():
            if splited[0] == "temperature":
                self.graph(source, dst)

    def graph(self, *args):
        parms = [
            '-v', '°C',
                'DEF:temp_avg={file}:value:AVERAGE',
                'DEF:temp_min={file}:value:MIN',
                'DEF:temp_max={file}:value:MAX',
                "AREA:temp_max#$HalfRed",
                "AREA:temp_min#$Canvas",
                "LINE1:temp_avg#$FullRed:Temperature",
                'GPRINT:temp_min:MIN:%4.1lf Min,',
                'GPRINT:temp_avg:AVERAGE:%4.1lf Avg,',
                'GPRINT:temp_max:MAX:%4.1lf Max,',
                'GPRINT:temp_avg:LAST:%4.1lf Last\l',
        ]
        self.gen_graph(parms, *args)
        
        
