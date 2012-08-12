from plugin import MetaPluginSum, MetaPluginLine

class Swap(MetaPluginSum):
    plugin_directory = "swap"
    dst_name = "swap"

    def graph_meta(self, *args):
        values = (
            ('used', 'ff0000', 'swap-used.rrd', "value"),
            ('cached', '0000ff', 'swap-cached.rrd', "value"),
            ('free', '00e000', 'swap-free.rrd', "value"),
        )
        return super(Swap, self).graph_meta(values, *args)

class SwapIO(MetaPluginLine):
    plugin_directory = "swap"
    dst_name = "swap"

    def gen(self):
        self.graph_meta_io("swap_io-%s.png")

    def graph_meta_io(self, *args):
        values = (
            ('in', '0077FF', 'swap_io-in.rrd', "value"),
            ('out', 'ffb000', 'swap_io-out.rrd', "value"),
        )
        return super(SwapIO, self).graph_meta(values, *args)