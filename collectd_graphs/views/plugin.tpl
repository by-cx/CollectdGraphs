<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Collectd statistics</title>
    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
    <script src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
    
</head>
<body>

    <div data-role="page"> 
        <div data-role="header">
            <a href="/#{{ machine }}" data-role="button">Plugins list</a>
            <h1>{{ plugin }} on {{ machine }}</h1>
            <a href="/all" data-role="button" rel="external">Regenerate all graphs</a>
        </div>
        <div data-role="content">
        %for graph in data:
            <p><strong>{{ graph }}</strong></p>
            <div data-role="controlgroup" data-type="horizontal">
                %for time in ("day", "week", "month", "three-months", "six-months", "year"):
                    <a href="/plugin/{{ machine }}/{{ plugin }}/{{ time }}" data-role="button">{{ time }}</a>
                %end
                </div>
            <p><img src="/static/{{ machine }}/{{ plugin }}/{{ graph }}" alt="{{ graph }}"></p>
        %end
        </div>
        <div data-role="footer"><h2>Developed by <a href="mailto:cx@initd.cz">Adam Štrauch</a> for <a href="http://best-hosting.cz">BEST-HOSTING</a></h2></div> 
    </div> 

</body>
</html>