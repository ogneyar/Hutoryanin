(function(){

    var doc = document;

    doc.addEventListener("DOMContentLoaded", function(){
        //console.log("Страница загрузилась!");
        
        var about = doc.getElementById('about');
        var text = doc.getElementById('about-text');

		about.onclick = function() {
            if (text.style.display == "block") {
                text.style.display = "none";
                about.innerHTML = "<h4>Обо мне.</h4>";
                about.style.color = "black";
                about.style.border = "2px solid black";
            }else {
                text.style.display = "block";
                about.innerHTML = "<h4>Скрыть текст.</h4>";
                about.style.color = "red";
                about.style.border = "2px solid red";
            }

            //предотвращаем переход по ссылке href
            return false;
        }
        console.log(about);
	});	

})();