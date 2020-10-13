(function(){
	var doc = document,
		div = doc.createElement("div"),
		body = doc.getElementById("body");
	
	//doc.writeln("Hell o world!");
	
	div.innerHTML = "<br><br><br><br><br><center><h1>Hell o world!</h1></center>";
	
	div.style.color = "red";
	div.id = "div";
	
	div.onclick = function(){
	    if (this.style.color == "blue") this.style.color = "red";
	    else this.style.color = "blue";
	}
	
	//div.onclick = myfunc(div);
	
	body.parentNode.appendChild(div);
})();

/*
function myfunc(var el){
    if (el.style.color == "blue")
        el.style.color = "red";
	else 
	    el.style.color = "blue";
	return false;
}
*/
