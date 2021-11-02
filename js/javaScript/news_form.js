function check () { 
    var title = document.getElementById("title").value; 
    var radios = document.getElementsByName('type'); 

    for (var i = 0, length = radios.length; i < length; i++) { 
        if (radios[i].checked) { 
            var type = radios[i].value; 

            break; 
        } 
    } 

    var intro = document.getElementById("intro").value; 

    if (title == "") 
      document.getElementById("mess").innerHTML = "Введите заголовок для статьи<br><br>"; 
    else if (intro == "") 
        document.getElementById("mess").innerHTML = "Введите анонс для статьи<br><br>"; 
    else { 
      alert ("Все отлично, статья опубликована"); 
      document.getElementById("articles").innerHTML = "<h2>" + title + "</h2><p>" + intro + "</p>"; 
    } 
  }