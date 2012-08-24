function set_key(key, value){
	$.post(
		"/key/set",
		{key: key, value: value},
		function (data) {
			if (data["status"] != "ok") alert("Error during communication with server!");
		}
	)
}

function get_key(key){
	var value = "";
	$.post(
		"/key/get",
		{key: key},
		function (data) {
			if (data["status"] != "ok") alert("Error during communication with server!");
			value = data["data"];
		}
	)
	return value;
}