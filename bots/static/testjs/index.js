(function(){
	var doc = document,
		body = doc.body,
		/*div = doc.createElement("div"),*/
		div_head_image = doc.createElement("div"),
		a_head_image = doc.createElement("a"),
		img1 = doc.createElement("img"),
		div_menu = doc.createElement("div"),
		div_line_menu = doc.createElement("div"),
		a_home = doc.createElement("a");
	
	/*body.className = "body";*/
	
	div_head_image.className = "head_image";	
	a_head_image.href = "/";	
	img1.src = "/static/logo.png";
	img1.alt = "Логотип Руна Йера";
	a_head_image.appendChild(img1);
	div_head_image.appendChild(a_head_image);	
	body.appendChild(div_head_image);
	
	div_menu.className = "menu";
	div_line_menu.className = "line-menu logo";
	a_home.href = "/";
	a_home.innerHTML = "ХуторянинЪ";
	a_home.className = "btn btn-danger home";
	div_line_menu.appendChild(a_home);
	div_menu.appendChild(div_line_menu);	
	body.appendChild(div_menu);

	/*div.className = "div";
	div.innerHTML = "Hell o world!";
	div.id = "div";
	body.appendChild(div);	
	div.onclick = function(){
		funcForDiv(div);
	}*/

	body.onclick = function(){
		funcForBody(body);
	}



	//doc.writeln("Hell o world!");		
	/*
	div.style.color = "blue";
	div.style.userSelect = "none";
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






