for (var i = 0; i < 10; i++) 
    console.log(i);


var ii = 1;
while (ii <= 10) {  
    console.log(ii); 
    ii++; 
}

var x = 13; 
do { 
    x--; 
    console.log(x); 
} while (x > 10);


for(var i = 10; i <= 20; i += 2) { 
    if(i > 15) 
        break; 
   
    console.log(i); 
} 
   
for(var i = 10; i <= 20; i++) { 
    if(i % 2 == 0) 
        continue; 
   
    console.log(i); 
}



var arr = [5, 7, 3, 8, 9, 91]; 
 
for(var i = 0; i < arr.length; i++) { 
    arr[i] *= 2; 
 
    console.log("Элемент " + (i + 1) + ": " + arr[i]); 
} 