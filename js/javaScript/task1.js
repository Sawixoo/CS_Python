function task_1_1(age){
    //check age
    if(age>=18)
        return true;
    else
        return confirm("Родители разрешили?");
}

task_1_1(18);


var count = 0;
function task_1_2(){
    count ++;
    console.log("Количество вводов: " + count);
}
task_1_2();
task_1_2();


function task_1_3(km, hour) {
    //km_count
    var res = km*hour;
    task_1_4(res);
    return res;
}

function task_1_4(res) {
    //print(res)
	var word = res == 1 ? "Вы проедете: 1 километр" : "Вы проедете: " + res + " километров";
	console.log(word);
}

var res = task_1_3(21, 2.4);


