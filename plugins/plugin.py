class Plugin(object):
    def __init__(self, data_dir, dst_dir, size=(800, 350)):
        self.data_dir = data_dir
        self.dst_dir = dst_dir
        self.filenames = {}
        self.site = size

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
