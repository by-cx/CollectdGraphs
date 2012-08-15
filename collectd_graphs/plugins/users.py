from plugin import Plugin

class Users(Plugin):
    plugin_directory = "users"
    dst_name = "users"

    def gen(self):
        self.graph_users("users.rrd" ,"users-%s.png")
        
    def graph_users(self, *args):
        parms = [
                '-v', 'Users',
                'DEF:users_avg={file}:users:AVERAGE',
                'DEF:users_min={file}:users:MIN',
                'DEF:users_max={file}:users:MAX',
                "AREA:users_max#$HalfBlue",
                "AREA:users_min#$Canvas",
                "LINE1:users_avg#$FullBlue:Users",
                'GPRINT:users_min:MIN:%4.1lf Min,',
                'GPRINT:users_avg:AVERAGE:%4.1lf Average,',
                'GPRINT:users_max:MAX:%4.1lf Max,',
                'GPRINT:users_avg:LAST:%4.1lf Last\l',
        ]
        self.gen_graph(parms, *args)
