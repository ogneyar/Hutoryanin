(function(){
	var doc = document,
		body = doc.body,
		div = doc.createElement("div");		
		
	body.className = "body";
	div.className = "div";
	div.innerHTML = "Hell o world!";
	div.id = "div";
	body.appendChild(div);	
	div.onclick = function(){
		funcForDiv(div);
	}
	body.onclick = function(){
		funcForBody(body);
	}
	//doc.writeln("Hell o world!");		
	/*
	div.style.color = "blue";
	div.style.userSelect = "none";
	*/	
	/*
	div.onclick = function(){
	    if (this.style.color == "blue") this.style.color = "red";
	    else this.style.color = "blue";
	}
	*/
	//body.parentNode.appendChild(div);
})();


function funcForBody(element){	
    if (element.style.backgroundColor == "lightgrey") {
        element.style.backgroundColor = "white";
	}else {
	    element.style.backgroundColor = "lightgrey";
	}	
	
}
function funcForDiv(element){	
	if (element.className == "div2") {		
        element.className = "div";
	}else {
	    element.className = "div2";
}	
/*
    if (element.style.color == "red") {		
        element.style.color = "blue";
		//console.log("zzz");
	}else {
	    element.style.color = "red";
		//console.log("ggg");
	}	
*/
}






