from plugin import Plugin

class Load(Plugin):
	plugin_directory = "load"

	def __init__(self, *args, **kwargs):
		super(Load, self).__init__(*args, **kwargs)
        self.gen()

	def gen(self):
		self.gen_graph("%s.rrd" % self.plugin_directory, "%s.png" % self.plugin_directory)

	def gen_graph(self, *args):
		parms = [
			'-v', 'System load',
			'DEF:s_avg={file}:shortterm:AVERAGE',
			'DEF:s_min={file}:shortterm:MIN',
			'DEF:s_max={file}:shortterm:MAX',
			'DEF:m_avg={file}:midterm:AVERAGE',
			'DEF:m_min={file}:midterm:MIN',
			'DEF:m_max={file}:midterm:MAX',
			'DEF:l_avg={file}:longterm:AVERAGE',
			'DEF:l_min={file}:longterm:MIN',
			'DEF:l_max={file}:longterm:MAX',
			"AREA:s_max#$HalfGreen",
			"AREA:s_min#$Canvas",
			"LINE1:s_avg#$FullGreen: 1m average",
			'GPRINT:s_min:MIN:%4.2lf Min,',
			'GPRINT:s_avg:AVERAGE:%4.2lf Avg,',
			'GPRINT:s_max:MAX:%4.2lf Max,',
			'GPRINT:s_avg:LAST:%4.2lf Last\n',
			"LINE1:m_avg#$FullBlue: 5m average",
			'GPRINT:m_min:MIN:%4.2lf Min,',
			'GPRINT:m_avg:AVERAGE:%4.2lf Avg,',
			'GPRINT:m_max:MAX:%4.2lf Max,',
			'GPRINT:m_avg:LAST:%4.2lf Last\n',
			"LINE1:l_avg#$FullRed:15m average",
			'GPRINT:l_min:MIN:%4.2lf Min,',
			'GPRINT:l_avg:AVERAGE:%4.2lf Avg,',
			'GPRINT:l_max:MAX:%4.2lf Max,',
			'GPRINT:l_avg:LAST:%4.2lf Last',
		]
		super(Load, self).gen_graph(parms, *args)