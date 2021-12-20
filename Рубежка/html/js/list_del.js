const input = document.querySelector('#input');
const btn = document.querySelector('#btn');
const result = document.querySelector('#result');

btn.addEventListener('click', (e) =>{
    if (input.value ==='') return
    createDeleteElements(input.value)
    input.value = ''
})

function createDeleteElements(value){
    const li = document.createElement('li');
    var span = document.createElement('span');

    li.textContent = value;
    result.appendChild(li);
}

result.addEventListener('dblclick', function(evt) { 
    result.removeChild(evt.target);
},false);