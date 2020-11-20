(function(){

    var doc = document;

    doc.addEventListener("DOMContentLoaded", function(){
        //console.log("Страница загрузилась!");
        
        var about = doc.getElementById('about');
        var text = doc.getElementById('about-text');

        // функция для работы кнопки "ОБО МНЕ" на главной странице
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
        //console.log(about);

    });	

    
    var submit_sendmail = doc.getElementsByClassName('submit_sendmail');
    var section = doc.getElementById('section');

    // функция для показа заставки во время отправки сообщения на почту
    submit_sendmail[0].onclick = function() {
        section.style.display = "block";

        //return false;
    }

})();