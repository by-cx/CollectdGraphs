import os
import re
from plugin import Plugin
import rrdtool

class Interface(Plugin):
    def __init__(self, *args, **kwargs):
        super(Interface, self).__init__(*args, **kwargs)
        self.scan_for_files()

    def scan_for_files(self):
        data_dir = os.path.join(self.data_dir, "interface")
        for filename in os.listdir(data_dir):
            s = re.search("^if_([a-z]*)\-([a-z0-9]*)\.rrd", filename)
            if s:
                datetype, interface = s.groups()
                if datetype == "packets":
                    dst_path = os.path.join(
                        self.dst_dir,
                        "interface",
                        filename[:-4] + "-%s.png",
                    )
                    self.graph_if_packets(
                        os.path.join(data_dir, filename),
                        dst_path,
                    )

            #if_errors-eth0.rrd  if_octets-eth0.rrd  if_packets-eth0.rrd

    def graph_if_packets(self, rrd_path, dst_path):
        parms = [
            '--start','{START}', '--end', '-1',
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
            'GPRINT:rx_avg_sum:LAST:(ca. %4.0lf%s Total)\l',
        ]
        for name, time_range in self.time_ranges():
            rrdtool.graph(dst_path % name, self.convert(parms, rrd_path, time_range))


        

