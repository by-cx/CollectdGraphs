from plugin import Plugin

class Snmp(Plugin):
    plugin_directory = "snmp"
    dst_name = "snmp"

    def gen(self):
        for splited, source, dst in self.scan_for_files():
            if splited[0] == "if_octets":
                self.graph_if_octets(source, dst)
        
    def graph_if_octets(self, *args):
        parms = [
            '-v', 'Bits/s', '--units=si',
            'DEF:out_min_raw={file}:tx:MIN',
            'DEF:out_avg_raw={file}:tx:AVERAGE',
            'DEF:out_max_raw={file}:tx:MAX',
            'DEF:inc_min_raw={file}:rx:MIN',
            'DEF:inc_avg_raw={file}:rx:AVERAGE',
            'DEF:inc_max_raw={file}:rx:MAX',
            'CDEF:out_min=out_min_raw,8,*',
            'CDEF:out_avg=out_avg_raw,8,*',
            'CDEF:out_max=out_max_raw,8,*',
            'CDEF:inc_min=inc_min_raw,8,*',
            'CDEF:inc_avg=inc_avg_raw,8,*',
            'CDEF:inc_max=inc_max_raw,8,*',
            'CDEF:overlap=out_avg,inc_avg,GT,inc_avg,out_avg,IF',
            'CDEF:mytime=out_avg_raw,TIME,TIME,IF',
            'CDEF:sample_len_raw=mytime,PREV(mytime),-',
            'CDEF:sample_len=sample_len_raw,UN,0,sample_len_raw,IF',
            'CDEF:out_avg_sample=out_avg_raw,UN,0,out_avg_raw,IF,sample_len,*',
            'CDEF:out_avg_sum=PREV,UN,0,PREV,IF,out_avg_sample,+',
            'CDEF:inc_avg_sample=inc_avg_raw,UN,0,inc_avg_raw,IF,sample_len,*',
            'CDEF:inc_avg_sum=PREV,UN,0,PREV,IF,inc_avg_sample,+',
            "AREA:out_avg#$HalfGreen",
            "AREA:inc_avg#$HalfBlue",
            "AREA:overlap#$HalfBlueGreen",
            "LINE1:out_avg#$FullGreen:Outgoing",
            'GPRINT:out_avg:AVERAGE:%5.1lf%s Avg,',
            'GPRINT:out_max:MAX:%5.1lf%s Max,',
            'GPRINT:out_avg:LAST:%5.1lf%s Last',
            'GPRINT:out_avg_sum:LAST:(ca. %5.1lf%sB Total)\l',
            "LINE1:inc_avg#$FullBlue:Incoming",
        ]
        self.gen_graph(parms, *args)
