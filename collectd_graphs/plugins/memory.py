from plugin import MetaPluginSum

class Memory(MetaPluginSum):
    plugin_directory = "memory"
    dst_name = "memory"

    def gen(self):
        self.graph_meta("memory-%s.png")

    def graph_meta(self, *args):
        values = (
            ('used', 'ff0000', 'memory-used.rrd', "value"),
            ('buffered', 'ffb000', 'memory-buffered.rrd', "value"),
            ('cached', '0000ff', 'memory-cached.rrd', "value"),
            ('free', '00e000', 'memory-free.rrd', "value"),
        )
        return super(Memory, self).graph_meta(values, *args)