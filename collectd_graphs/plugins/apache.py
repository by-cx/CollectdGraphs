from plugin import Plugin, MetaPluginSum
import os
import re

class Apache(Plugin):
    plugin_directory = "apache-[a-z0-9\-_]{1,32}"
    dst_name = "apache"

    def gen(self):
        for filename in os.listdir(self._data_dir):
            if re.match("apache-[a-z0-9\-_]{1,32}", filename):
                self.plugin_directory = filename
                self.graph_bytes("apache_bytes.rrd", filename + "-bytes-%s.png")
                self.graph_connections("apache_connections.rrd", filename + "-connections-%s.png")
                self.graph_idle_workers("apache_idle_workers.rrd", filename + "-idle_workers-%s.png")
                self.graph_requests("apache_requests.rrd", filename + "-requests-%s.png")


    def graph_bytes(self, *args):
        parms = [
            '-v', 'Bits/s',
            'DEF:min_raw={file}:count:MIN',
            'DEF:avg_raw={file}:count:AVERAGE',
            'DEF:max_raw={file}:count:MAX',
            'CDEF:min=min_raw,8,*',
            'CDEF:avg=avg_raw,8,*',
            'CDEF:max=max_raw,8,*',
            'CDEF:mytime=avg_raw,TIME,TIME,IF',
            'CDEF:sample_len_raw=mytime,PREV(mytime),-',
            'CDEF:sample_len=sample_len_raw,UN,0,sample_len_raw,IF',
            'CDEF:avg_sample=avg_raw,UN,0,avg_raw,IF,sample_len,*',
            'CDEF:avg_sum=PREV,UN,0,PREV,IF,avg_sample,+',
            "AREA:avg#$HalfBlue",
            "LINE1:avg#$FullBlue:Bit/s",
            'GPRINT:min:MIN:%5.1lf%s Min,',
            'GPRINT:avg:AVERAGE:%5.1lf%s Avg,',
            'GPRINT:max:MAX:%5.1lf%s Max,',
            'GPRINT:avg:LAST:%5.1lf%s Last',
            'GPRINT:avg_sum:LAST:(ca. %5.1lf%sB Total)\l',
        ]
        self.gen_graph(parms, *args)

    def graph_connections(self, *args):
        parms = [
            '-v', 'Connections/s',
            'DEF:min={file}:count:MIN',
            'DEF:avg={file}:count:AVERAGE',
            'DEF:max={file}:count:MAX',
            "AREA:max#$HalfBlue",
            "AREA:min#$Canvas",
            "LINE1:avg#$FullBlue:Connections/s",
            'GPRINT:min:MIN:%6.2lf Min,',
            'GPRINT:avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:max:MAX:%6.2lf Max,',
            'GPRINT:avg:LAST:%6.2lf Last',
        ]
        self.gen_graph(parms, *args)

    def graph_idle_workers(self, *args):
        parms = [
            '-v', 'Idle workers/s',
            'DEF:min={file}:count:MIN',
            'DEF:avg={file}:count:AVERAGE',
            'DEF:max={file}:count:MAX',
            "AREA:max#$HalfBlue",
            "AREA:min#$Canvas",
            "LINE1:avg#$FullBlue:Idle workers/s",
            'GPRINT:min:MIN:%6.2lf Min,',
            'GPRINT:avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:max:MAX:%6.2lf Max,',
            'GPRINT:avg:LAST:%6.2lf Last',
        ]
        self.gen_graph(parms, *args)

    def graph_requests(self, *args):
        parms = [
            '-v', 'Requests/s',
            'DEF:min={file}:count:MIN',
            'DEF:avg={file}:count:AVERAGE',
            'DEF:max={file}:count:MAX',
            "AREA:max#$HalfBlue",
            "AREA:min#$Canvas",
            "LINE1:avg#$FullBlue:Requests/s",
            'GPRINT:min:MIN:%6.2lf Min,',
            'GPRINT:avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:max:MAX:%6.2lf Max,',
            'GPRINT:avg:LAST:%6.2lf Last',
        ]
        self.gen_graph(parms, *args)

class ApacheScoreboard(MetaPluginSum):
    plugin_directory = "apache-[a-z0-9\-_]{1,32}"
    dst_name = "apache"

    def gen(self):
        for filename in os.listdir(self._data_dir):
            if re.match("apache-[a-z0-9\-_]{1,32}", filename):
                self.graph_meta_scoreboard(filename  + "scoreboard-%s.png")

    def graph_meta_scoreboard(self, *args):
        values = (
            ('open', '00e000', 'apache_scoreboard-open.rrd', 'count'),
            ('waiting', '0000ff', 'apache_scoreboard-waiting.rrd', 'count'),
            ('starting', 'a00000', 'apache_scoreboard-starting.rrd', 'count'),
            ('reading', 'ff0000', 'apache_scoreboard-reading.rrd', 'count'),
            ('sending', '00ff00', 'apache_scoreboard-sending.rrd', 'count'),
            ('keepalive', 'f000f0', 'apache_scoreboard-keepalive.rrd', 'count'),
            ('dnslookup', '00a000', 'apache_scoreboard-dnslookup.rrd', 'count'),
            ('logging', '008080', 'apache_scoreboard-logging.rrd', 'count'),
            ('closing', 'a000a0', 'apache_scoreboard-closing.rrd', 'count'),
            ('finishing', '000080', 'apache_scoreboard-finishing.rrd', 'count'),
            ('idle_cleanup', '000000', 'apache_scoreboard-idle_cleanup.rrd', 'count'),
        )
        return super(ApacheScoreboard, self).graph_meta(values, *args)
