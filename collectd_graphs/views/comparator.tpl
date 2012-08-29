<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Collectd statistics - comparator</title>
    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
    <script src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
    <script src="/static/keyvalue.js"></script>
</head>
<body>
    <div data-role="page"> 
        <div data-role="header">
            <h1>Comparator {{ comparator }}</h1>
            <a href="/" data-role="button" rel="external">Machines list</a>
        </div>
        <div data-role="content">
            %for machine, plugin, time, graph in graphs:
                <p>
                    <h3>{{ machine }}</h3>
                    <a href="/comparator/delete/{{ comparator }}/{{ machine }}/{{ plugin }}/{{ time }}/{{ graph }}"><img src="/graph/{{ machine }}/{{ plugin }}/{{ graph }}" alt="{{ graph }}"></a>
                </p>
            %end
        </div>
        <div data-role="footer">
            <h4>Developed by <a href="mailto:cx@initd.cz">Adam Štrauch</a> for <a href="http://best-hosting.cz">BEST-HOSTING</a></h4>
        </div> 
    </div> 

</body>
</html>
