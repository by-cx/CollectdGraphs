import os
import re
import rrdtool

class Plugin(object):
    def __init__(self, data_dir, dst_dir, size=(400, 120)):
        """
            Basic class for plugin_directory

            data_dir - directory with rrd databases
            dst_dir - directory for graphs
            size - (x, y) tuple with size of graphs
        """
        self._data_dir = data_dir
        self._dst_dir = dst_dir
<<<<<<< HEAD
        self.filenames = {}
=======
>>>>>>> df85fdb4e320c9d483b022f05c78defbded075e0
        self.size = size

    @property
    def data_dir(self):
        return os.path.join(self._data_dir, self.plugin_directory)

    @property
    def dst_dir(self):
        directory = os.path.join(self._dst_dir, self.plugin_directory)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        return directory

    def time_ranges(self):
        return (
            ("day", "-1d"),
            ("week", "-1w"),
            ("month", "-4w"),
            ("three-months", "-12w"),
            ("six-months", "-24w"),
            ("year", "-1y"),
        )


    def convert(self, parms, path, end):
        """Convert variables in parameters
        """
        def convert_map(parm):
            parm = parm.replace("{file}", path)
            parm = parm.replace("{x}", "%d" % self.size[0])
            parm = parm.replace("{y}", "%d" % self.size[1])
            parm = parm.replace("$Canvas", "FFFFFF")
            parm = parm.replace("$FullRed", "FF0000")
            parm = parm.replace("$FullGreen", "00E000")
            parm = parm.replace("$FullBlue", "0000FF")
            parm = parm.replace("$FullYellow", "F0A000")
            parm = parm.replace("$FullCyan", "00A0FF")
            parm = parm.replace("$FullMagenta", "A000FF")
            parm = parm.replace("$HalfBlueGreen", "89B3C9")
            parm = parm.replace("$HalfRed", "F7B7B7")
            parm = parm.replace("$HalfGreen", "B7EFB7")
            parm = parm.replace("$HalfBlue", "B7B7F7")
            parm = parm.replace("$HalfYellow", "F3DFB7")
            parm = parm.replace("$HalfCyan", "B7DFF7")
            parm = parm.replace("$HalfMagenta", "DFB7F7")
            parm = parm.replace("{START}", end)
            return parm
        return map(convert_map, parms)

    def scan_for_files(self):
        files = []
        for filename in os.listdir(self.data_dir):
            if re.search("\.rrd$", filename):
                files.append((
                    filename[:-4].split("-"), # splited filename
                    "%s.rrd" % filename[:-4], # source rrd
                    filename[:-4] + "-%s.png", # dst png
                ))
        return files        

    def gen_graph(self, parms, source, dst):
        rrd_path = os.path.join(self.data_dir, source)
        graph_path = os.path.join(self.dst_dir, dst)

        parms_common = [
            '--start','{START}', '--end', '-1',
            '--width','{x}', '--height', '{y}',
        ]
        for name, time_range in self.time_ranges():
            rrdtool.graph(
                graph_path % name,
                self.convert(parms_common + parms, rrd_path, time_range)
            )

