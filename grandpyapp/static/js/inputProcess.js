fetch('https://www.google.com/maps/embed/v1/place?key=GOOGLEAPIKEY=louvre')
.then(function(res) {
	if (res.ok) {
		return res.json();
	}
})
.then(function(value){
	console.log(value);
})
.catch(function(err) {
	//une erreur est survenue
})