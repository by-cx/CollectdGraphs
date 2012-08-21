from plugin import Plugin

class Snmp(Plugin):
    plugin_directory = "snmp"
    dst_name = "snmp"

    def gen(self):
        for splited, source, dst in self.scan_for_files():
            if splited[0] == "if_octets":
                self.graph_if_octets(source, dst)
            elif splited[0] in ("if_packets", "if_uni_packets", "if_nuni_packets"):
                self.graph_if_packets(source, dst)
            elif splited[0] == "if_errors":
                self.graph_if_errors(source, dst)

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

    def graph_if_packets(self, *args):
        parms = [
            '-v', 'Packets/s', '--units=si',
            'DEF:tx_min={file}:tx:MIN',
            'DEF:tx_avg={file}:tx:AVERAGE',
            'DEF:tx_max={file}:tx:MAX',
            'DEF:rx_min={file}:rx:MIN',
            'DEF:rx_avg={file}:rx:AVERAGE',
            'DEF:rx_max={file}:rx:MAX',
            'CDEF:overlap=tx_avg,rx_avg,GT,rx_avg,tx_avg,IF',
            'CDEF:mytime=tx_avg,TIME,TIME,IF',
            'CDEF:sample_len_raw=mytime,PREV(mytime),-',
            'CDEF:sample_len=sample_len_raw,UN,0,sample_len_raw,IF',
            'CDEF:tx_avg_sample=tx_avg,UN,0,tx_avg,IF,sample_len,*',
            'CDEF:tx_avg_sum=PREV,UN,0,PREV,IF,tx_avg_sample,+',
            'CDEF:rx_avg_sample=rx_avg,UN,0,rx_avg,IF,sample_len,*',
            'CDEF:rx_avg_sum=PREV,UN,0,PREV,IF,rx_avg_sample,+',
            "AREA:tx_avg#$HalfGreen",
            "AREA:rx_avg#$HalfBlue",
            "AREA:overlap#$HalfBlueGreen",
            "LINE1:tx_avg#$FullGreen:TX",
            'GPRINT:tx_avg:AVERAGE:%5.1lf%s Avg,',
            'GPRINT:tx_max:MAX:%5.1lf%s Max,',
            'GPRINT:tx_avg:LAST:%5.1lf%s Last',
            'GPRINT:tx_avg_sum:LAST:(ca. %4.0lf%s Total)\l',
            "LINE1:rx_avg#$FullBlue:RX",
            #'GPRINT:rx_min:MIN:%5.1lf %s Min,',
            'GPRINT:rx_avg:AVERAGE:%5.1lf%s Avg,',
            'GPRINT:rx_max:MAX:%5.1lf%s Max,',
            'GPRINT:rx_avg:LAST:%5.1lf%s Last',
            'GPRINT:rx_avg_sum:LAST:(ca. %4.0lf%s Total)\l'
        ]
        self.gen_graph(parms, *args)

    def graph_if_errors(self, *args):
        parms = [
            '-v', 'Errors/s', '--units=si',
            'DEF:tx_min={file}:tx:MIN',
            'DEF:tx_avg={file}:tx:AVERAGE',
            'DEF:tx_max={file}:tx:MAX',
            'DEF:rx_min={file}:rx:MIN',
            'DEF:rx_avg={file}:rx:AVERAGE',
            'DEF:rx_max={file}:rx:MAX',
            'CDEF:overlap=tx_avg,rx_avg,GT,rx_avg,tx_avg,IF',
            'CDEF:mytime=tx_avg,TIME,TIME,IF',
            'CDEF:sample_len_raw=mytime,PREV(mytime),-',
            'CDEF:sample_len=sample_len_raw,UN,0,sample_len_raw,IF',
            'CDEF:tx_avg_sample=tx_avg,UN,0,tx_avg,IF,sample_len,*',
            'CDEF:tx_avg_sum=PREV,UN,0,PREV,IF,tx_avg_sample,+',
            'CDEF:rx_avg_sample=rx_avg,UN,0,rx_avg,IF,sample_len,*',
            'CDEF:rx_avg_sum=PREV,UN,0,PREV,IF,rx_avg_sample,+',
            "AREA:tx_avg#$HalfGreen",
            "AREA:rx_avg#$HalfBlue",
            "AREA:overlap#$HalfBlueGreen",
            "LINE1:tx_avg#$FullGreen:TX",
            'GPRINT:tx_avg:AVERAGE:%5.1lf%s Avg,',
            'GPRINT:tx_max:MAX:%5.1lf%s Max,',
            'GPRINT:tx_avg:LAST:%5.1lf%s Last',
            'GPRINT:tx_avg_sum:LAST:(ca. %4.0lf%s Total)\l',
            "LINE1:rx_avg#$FullBlue:RX",
            #'GPRINT:rx_min:MIN:%5.1lf %s Min,',
            'GPRINT:rx_avg:AVERAGE:%5.1lf%s Avg,',
            'GPRINT:rx_max:MAX:%5.1lf%s Max,',
            'GPRINT:rx_avg:LAST:%5.1lf%s Last',
            'GPRINT:rx_avg_sum:LAST:(ca. %4.0lf%s Total)\l',
        ]
        self.gen_graph(parms, *args)
