<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Choose comparator</title>
    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
    <script src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
    <script src="/static/keyvalue.js"></script>
</head>
<body>

<div data-role="dialog">
    
        <div data-role="header" data-theme="d">
            <h1>Add to comparator</h1>
        </div>

        <script type="text/javascript">
        function new_comparator() {
            var comparator = $("#comparator").val();
            url = "/comparator/add/"+ comparator +"/{{ machine }}/{{ plugin }}/{{ time }}/{{ graph }}";
            $.get(url);
            $("a").attr("href", url)
                .attr("data-role", "button")
                .attr("data-rel", "back")
                .attr("data-theme", "c")
                .html(comparator).button().click();
            //$("#new_comparators").append(link);
            $("#comparator").val("");
        }
        function add_to_comparator(comparator) {
            url = "/comparator/add/"+ comparator +"/{{ machine }}/{{ plugin }}/{{ time }}/{{ graph }}";
            $.get(url);
            $("a").attr("href", url)
                .attr("data-role", "button")
                .attr("data-rel", "back")
                .attr("data-theme", "c")
                .button().click();
        }
        </script>

        <div data-role="content" data-theme="c">
            <h1>New comparator</h1>
            <input type="text" data-mini="true" id="comparator">
            <button onclick="new_comparator()" data-rel="back" data-role="button" data-theme="b">Create new one</button>
            <h1>Choose existing comparator</h1>
            <span id="new_comparators"></span>
            %for comparator in comparators:
            <button onclick="add_to_comparator('{{ comparator }}')" data-role="button" data-rel="back" data-theme="c">{{ comparator }}</button>
            %end
            <a href="#" data-role="button" data-rel="back" data-theme="b">Cancel</a>
        </div>
    </div>


</body>
</html>
