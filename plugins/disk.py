import os
import re
from plugin import Plugin

class Disk(Plugin):
    dst_name = "disk"

    def __init__(self, *args, **kwargs):
        super(Disk, self).__init__(*args, **kwargs)
        self.gen()

    def gen(self):
        for filename in os.listdir(self._data_dir):
            if re.match("disk-[a-z0-9]{3,6}", filename):
                self.plugin_directory = filename
                self.graph_merged("disk_merged.rrd" ,filename + "-merged-%s.png")
                self.graph_octets("disk_octets.rrd" ,filename + "-octets-%s.png")
                self.graph_ops("disk_ops.rrd" ,filename + "-ops-%s.png")
                self.graph_time("disk_time.rrd" ,filename + "-time-%s.png")
        
    def graph_merged(self, *args):
        parms = [
            '-v', 'Merged Ops/s', '--units=si',
            'DEF:out_min={file}:write:MIN',
            'DEF:out_avg={file}:write:AVERAGE',
            'DEF:out_max={file}:write:MAX',
            'DEF:inc_min={file}:read:MIN',
            'DEF:inc_avg={file}:read:AVERAGE',
            'DEF:inc_max={file}:read:MAX',
            'CDEF:overlap=out_avg,inc_avg,GT,inc_avg,out_avg,IF',
            "AREA:out_avg#$HalfGreen",
            "AREA:inc_avg#$HalfBlue",
            "AREA:overlap#$HalfBlueGreen",
            "LINE1:out_avg#$FullGreen:Written",
            'GPRINT:out_avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:out_max:MAX:%6.2lf Max,',
            'GPRINT:out_avg:LAST:%6.2lf Last\l',
            "LINE1:inc_avg#$FullBlue:Read   ",
            'GPRINT:inc_avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:inc_max:MAX:%6.2lf Max,',
            'GPRINT:inc_avg:LAST:%6.2lf Last\l',
        ]
        self.gen_graph(parms, *args)

    def graph_octets(self, *args):
        parms = [
            '-v', 'Bytes/s', '--units=si',
            'DEF:out_min={file}:write:MIN',
            'DEF:out_avg={file}:write:AVERAGE',
            'DEF:out_max={file}:write:MAX',
            'DEF:inc_min={file}:read:MIN',
            'DEF:inc_avg={file}:read:AVERAGE',
            'DEF:inc_max={file}:read:MAX',
            'CDEF:overlap=out_avg,inc_avg,GT,inc_avg,out_avg,IF',
            'CDEF:mytime=out_avg,TIME,TIME,IF',
            'CDEF:sample_len_raw=mytime,PREV(mytime),-',
            'CDEF:sample_len=sample_len_raw,UN,0,sample_len_raw,IF',
            'CDEF:out_avg_sample=out_avg,UN,0,out_avg,IF,sample_len,*',
            'CDEF:out_avg_sum=PREV,UN,0,PREV,IF,out_avg_sample,+',
            'CDEF:inc_avg_sample=inc_avg,UN,0,inc_avg,IF,sample_len,*',
            'CDEF:inc_avg_sum=PREV,UN,0,PREV,IF,inc_avg_sample,+',
            "AREA:out_avg#$HalfGreen",
            "AREA:inc_avg#$HalfBlue",
            "AREA:overlap#$HalfBlueGreen",
            "LINE1:out_avg#$FullGreen:Written",
            'GPRINT:out_avg:AVERAGE:%5.1lf%s Avg,',
            'GPRINT:out_max:MAX:%5.1lf%s Max,',
            'GPRINT:out_avg:LAST:%5.1lf%s Last',
            'GPRINT:out_avg_sum:LAST:(ca. %5.1lf%sB Total)\l',
            "LINE1:inc_avg#$FullBlue:Read   ",
            'GPRINT:inc_avg:AVERAGE:%5.1lf%s Avg,',
            'GPRINT:inc_max:MAX:%5.1lf%s Max,',
            'GPRINT:inc_avg:LAST:%5.1lf%s Last',
            'GPRINT:inc_avg_sum:LAST:(ca. %5.1lf%sB Total)\l',
        ]
        self.gen_graph(parms, *args)

    def graph_ops(self, *args):
        parms = [
            '-v', 'Ops/s', '--units=si',
            'DEF:out_min={file}:write:MIN',
            'DEF:out_avg={file}:write:AVERAGE',
            'DEF:out_max={file}:write:MAX',
            'DEF:inc_min={file}:read:MIN',
            'DEF:inc_avg={file}:read:AVERAGE',
            'DEF:inc_max={file}:read:MAX',
            'CDEF:overlap=out_avg,inc_avg,GT,inc_avg,out_avg,IF',
            "AREA:out_avg#$HalfGreen",
            "AREA:inc_avg#$HalfBlue",
            "AREA:overlap#$HalfBlueGreen",
            "LINE1:out_avg#$FullGreen:Written",
            'GPRINT:out_avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:out_max:MAX:%6.2lf Max,',
            'GPRINT:out_avg:LAST:%6.2lf Last\l',
            "LINE1:inc_avg#$FullBlue:Read   ",
            'GPRINT:inc_avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:inc_max:MAX:%6.2lf Max,',
            'GPRINT:inc_avg:LAST:%6.2lf Last\l',
        ]
        self.gen_graph(parms, *args)


    def graph_time(self, *args):
        parms = [
            '-v', 'Seconds/s',
            'DEF:out_min_raw={file}:write:MIN',
            'DEF:out_avg_raw={file}:write:AVERAGE',
            'DEF:out_max_raw={file}:write:MAX',
            'DEF:inc_min_raw={file}:read:MIN',
            'DEF:inc_avg_raw={file}:read:AVERAGE',
            'DEF:inc_max_raw={file}:read:MAX',
            'CDEF:out_min=out_min_raw,1000,/',
            'CDEF:out_avg=out_avg_raw,1000,/',
            'CDEF:out_max=out_max_raw,1000,/',
            'CDEF:inc_min=inc_min_raw,1000,/',
            'CDEF:inc_avg=inc_avg_raw,1000,/',
            'CDEF:inc_max=inc_max_raw,1000,/',
            'CDEF:overlap=out_avg,inc_avg,GT,inc_avg,out_avg,IF',
            "AREA:out_avg#$HalfGreen",
            "AREA:inc_avg#$HalfBlue",
            "AREA:overlap#$HalfBlueGreen",
            "LINE1:out_avg#$FullGreen:Written",
            'GPRINT:out_avg:AVERAGE:%5.1lf%ss Avg,',
            'GPRINT:out_max:MAX:%5.1lf%ss Max,',
            'GPRINT:out_avg:LAST:%5.1lf%ss Last\l',
            "LINE1:inc_avg#$FullBlue:Read   ",
            'GPRINT:inc_avg:AVERAGE:%5.1lf%ss Avg,',
            'GPRINT:inc_max:MAX:%5.1lf%ss Max,',
            'GPRINT:inc_avg:LAST:%5.1lf%ss Last\l',
        ]
        self.gen_graph(parms, *args)