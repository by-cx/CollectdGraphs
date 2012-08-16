from plugin import MetaPluginSum

class DNS(MetaPluginSum):
    plugin_directory = "dns"
    dst_name = "dns"

    def gen(self):
        self.graph_meta_qtype("-%s.png")

    def graph_meta_qtype(self, *args):
        values = (
            ('A6', '00e000', 'dns_qtype-A6.rrd', "value"),
            ('AAAA', '0000ff', 'dns_qtype-AAAA.rrd', "value"),
            ('ANY', 'ffb000', 'dns_qtype-ANY.rrd', "value"),
            ('A', 'ff0000', 'dns_qtype-A.rrd', "value"),
            ('CNAME', 'ff00ff', 'dns_qtype-CNAME.rrd', "value"),
            ('MX', 'a000a0', 'dns_qtype-MX.rrd', "value"),
            ('NS', '000000', 'dns_qtype-NS.rrd', "value"),
            ('PTR', '46C43B', 'dns_qtype-PTR.rrd', "value"),
            ('SOA', 'A9AD40', 'dns_qtype-SOA.rrd', "value"),
            ('SRV', 'C23939', 'dns_qtype-SRV.rrd', "value"),
            ('TXT', '65929F', 'dns_qtype-TXT.rrd', "value"),
        )

        return super(CPU, self).graph_meta(values, *args)
