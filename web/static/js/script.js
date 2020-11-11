(function(){

    var doc = document;

    doc.addEventListener("DOMContentLoaded", function(){
        console.log("Страница загрузилась!");
        
        var about = doc.getElementById('about');
        var text = doc.getElementById('about-text');
        // about.onclick.style.color = "red";
		about.onclick = function() {
            //this.style.color = "red";
            if (text.style.display == "block") {
                text.style.display = "none";
            }else text.style.display = "block";

            //предотвращаем переход по ссылке href
            return false;
        }
	});	

})();