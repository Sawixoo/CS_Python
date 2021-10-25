var a = 2, b = 10; 
if (a == b) { 
  console.log("a == b"); 
} else if (a <= b) {
  console.log("a <= b"); 
} else { 
  console.log("a > b"); 
}


var x = 23; 
switch (x) { 
  case  1: 
    console.log("Переменная равна 1"); 
    break; 
  case  56:
    console.log("Переменная равна 56"); 
    break;
  default: 
    console.log("Что-то другое"); 
    break;
}


var y = 90, a = 8; 
var res = y < a ? (y + a) : (y - a); 
console.log(res);


var number = 15; 
var isHasHouse = true; 
 
if(number == 15 && !isHasHouse) { 
  console.log("Ok"); 
} else if(number < 10) { 
  console.log("Ok!"); 
} else if(number == 7) { 
  console.log("7!"); 
} else if(number > 15) { 
  console.log("> 15!"); 
} else { 
  console.log("Else!"); 
}


var stroka = "word23"; 
 
switch(stroka) { 
  case 4: 
    console.log("Переменная со значением 4"); 
    break; 
  case "45": 
    console.log("Переменная со значением 45"); 
    break; 
  case "word": 
    console.log("Переменная со значением «word»"); 
    break; 
  default: 
    console.log("Default"); 
    break; 
}


