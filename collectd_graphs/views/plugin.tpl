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
            <a href="/all" data-role="button">Regenerate all graphs</a>
        </div>
        <div data-role="content">
        %for graph in data:
            <p><strong>{{ graph }}</strong></p>
            <p><img src="/static/{{ machine }}/{{ plugin }}/{{ graph }}" alt="{{ graph }}"></p>
        %end
        </div> 
    </div> 

</body>
</html>