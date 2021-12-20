document.getElementById('main-form').addEventListener("submit", checkForm);
function checkForm(event) {
    event.preventDefault();
    var el = document.getElementById('main-form');
    var name = el.user_name.value;
    var email = el.user_email.value;
    var phone = el.user_phone.value;
    var mess = el.user_sms.value;
    var fail = "";

    if (name == "" || email == "" || phone == "" || mess =="")
        fail = "Заполните все поля";
    else if (email.indexOf('@') === -1)
        fail = "Ошибка при вводе Email. Нет символа @ ";
    else if (mess.length <= 50 || mess.length > 400)
        fail = "Ваше сообщение не соответствует требуемым лимитам";


    if ( fail != "")
        document.getElementById('output_error').innerHTML = fail;

    else{
        // document.getElementById('user_name').value = "";
        // document.getElementById('user_email').value = "";
        // document.getElementById('user_phone').value = "";
        // document.getElementById('user_sms').value = "";

        document.getElementById('comment').innerHTML += `<div style="padding: 30px; border: 1px solid black; background: grey; margin: 5px"> 
        Email: ${email} <br>  
        Name: ${name} <br> 
        Phone: ${phone} <br> 
        ${mess} 
        </div>`;

        el.user_name.value = "";
        el.user_name.style.border = "5px solid green";

        el.user_email.value = "";
        el.user_email.style.border = "5px solid green";

        el.user_phone.value = "";
        el.user_phone.style.border = "5px solid green";

        el.user_sms.value = "";
        el.user_sms.style.border = "5px solid green";

        document.getElementById('btn').value = "Готово!";

        

    }

}