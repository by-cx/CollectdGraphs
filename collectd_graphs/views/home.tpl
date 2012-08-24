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
    
    <div data-role="page" id="home"> 
        <div data-role="header">
            <h1>Collectd statictics</h1>
        </div>
        
        <div data-role="content">
        <h2>Machines</h2>
            %for x in sorted(data):
            <p><a href="#{{ x }}" data-role="button">{{ x }}</a></p>
            %end
        </div> 
        <div data-role="footer">
            <h4>Developed by <a href="mailto:cx@initd.cz">Adam Štrauch</a> for <a href="http://best-hosting.cz">BEST-HOSTING</a></h4>
        </div> 
    </div> 

    %for machine in data:
    <div data-role="page" id="{{ machine }}">
        <div data-role="header">
            <a href="#home" data-role="button">Home</a>
            <h1>Plugins on {{ machine }}</h1>
        </div>
        <div data-role="content">
        <h2>Plugins on {{ machine }}</h2>
            %for plugin in sorted(data[machine]):
                <strong>{{ plugin }}</strong><br>
                <div data-role="controlgroup" data-type="horizontal">
                %for time in ("day", "week", "month", "three-months", "six-months", "year"):
                    <a href="/plugin/{{ machine }}/{{ plugin }}/{{ time }}" data-role="button">{{ time }}</a>
                %end
                </div>
            %end
        </div> 
        <div data-role="footer">
            <h4>Developed by <a href="mailto:cx@initd.cz">Adam Štrauch</a> for <a href="http://best-hosting.cz">BEST-HOSTING</a></h4>
        </div> 
    </div> 
    %end
    
</body>
</html>
