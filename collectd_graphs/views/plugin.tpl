<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Collectd statistics</title>
    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
    <script src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
    <script src="/static/keyvalue.js"></script>
</head>
<body>
    <div data-role="page"> 
        <div data-role="header">
            <a href="/#{{ machine }}" data-role="button" rel="external">Plugins list</a>
            <h1>{{ plugin }} on {{ machine }}</h1>
            <a href="/" data-role="button" rel="external">Machines list</a>
        </div>
        <div data-role="content">

                <h3>Intervals</h3>
                <div data-role="controlgroup" data-type="horizontal">
                    %for listed_time in ("day", "week", "month", "three-months", "six-months", "year"):
                        <a href="/plugin/{{ machine }}/{{ plugin }}/{{ listed_time }}" data-role="button">{{ listed_time }}</a>
                    %end
                </div>

                <div data-role="controlgroup" data-type="horizontal">
                <h3>Plugins</h3>
                %for listed_plugin in sorted(plugins):
                    <a href="/plugin/{{ machine }}/{{ listed_plugin }}/{{ time }}" data-role="button">{{ listed_plugin }}</a>
                %end
                </div>

                %for graph in sorted(data):
                    <p><img src="/graph/{{ machine }}/{{ plugin }}/{{ graph }}" alt="{{ graph }}"></p>
                %end

        </div>
        <div data-role="footer">
            <h4>Developed by <a href="mailto:cx@initd.cz">Adam Štrauch</a> for <a href="http://best-hosting.cz">BEST-HOSTING</a></h4>
        </div> 
    </div> 

</body>
</html>
