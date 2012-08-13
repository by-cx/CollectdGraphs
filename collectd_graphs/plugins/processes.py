from plugin import MetaPluginSum, Plugin

class Processes(MetaPluginSum):
    plugin_directory = "processes"
    dst_name = "processes"

    def graph_meta(self, *args):
        values = (
            ('running', '00e000', 'ps_state-running.rrd', 'value'),
            ('sleeping', '0000ff', 'ps_state-sleeping.rrd', 'value'),
            ('paging', 'ffb000', 'ps_state-paging.rrd', 'value'),
            ('zombies', 'ff0000', 'ps_state-zombies.rrd', 'value'),
            ('blocked', 'ff00ff', 'ps_state-blocked.rrd', 'value'),
            ('stopped', 'a000a0', 'ps_state-stopped.rrd', 'value'),
        )
        return super(Processes, self).graph_meta(values, *args)

class ForkRate(Plugin):
    plugin_directory = "processes"
    dst_name = "processes"

    def gen(self):
        self.graph_fork_rate("fork_rate.rrd", "fork_rate-%s.png")
        
    def graph_fork_rate(self, *args):
        parms = [
            '-v', 'Forks/s', '--units=si',
            'DEF:value_min={file}:value:MIN',
            'DEF:value_avg={file}:value:AVERAGE',
            'DEF:value_max={file}:value:MAX',
            "LINE1:value_avg#$FullBlue:Fork ",
            'GPRINT:value_avg:AVERAGE:%6.2lf Avg,',
            'GPRINT:value_max:MAX:%6.2lf Max,',
            'GPRINT:value_avg:LAST:%6.2lf Last\l',
        ]
        self.gen_graph(parms, *args)