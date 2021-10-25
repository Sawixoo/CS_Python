alert("Просто вывод информации"); 


var result = confirm("Вы согласны с confirm?");


var info = prompt("Сколько вам лет?", 25);


var person = null; 
if(confirm("Вы точно уверены?")) { 
    person = prompt("Введите ваше имя"); 
    alert("Привет, " + person); 
} else { 
    alert("Вы нажали на «Отмена»"); 
}