<?php
$name = $_POST['name'];
$email = $_POST['email'];
$site = $_POST['site'];
$coment = $_POST['coment'];
$state = $_POST['state'];
$pattern = "/^[a-zA-Z ]*$/";
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coment</title>
</head>

<body>
    <h1>Форма коментариев</h1>
    <form method="post" action="">
        <p> <span>Имя: </span><input type="text" name="name" placeholder="Введите ваше имя...">*
            <?php
            if ((strlen(trim($name)) <= 5) || (preg_match($pattern, $name))) {
                echo ' Имя не менее 5 символов, без пробелов и латиницы';
                $name = "";
            }
            ?>
        </p>
        <p> <span>Email: </span><input type="text" name="email" placeholder="Введите ваш Email...">*
            <?php
            if (filter_var($email, FILTER_VALIDATE_EMAIL) != true) {
                echo 'Email введен не верно';
                $email = "";
            }

            ?>
        </p>
        <p> <span>Сайт: </span><input type="text" name="site" placeholder="Введите адрес вашего сайта...">*
            <?php
            if (strlen(trim($site)) <= 5) {
                echo ' Сайт не менее 5 символов';
                $site = "";
            }
            ?>
        </p>

        <p> <span>Коментарий: </span><textarea name="coment" cols="40" rows="4" name="coment" placeholder="Введите ваш коментарий..."></textarea>*
            <?php
            if (strlen(trim($coment)) <= 50) {
                echo ' Коментарий не менее 50 символов';
                $coment = "";
            }
            ?>
        </p>

        <p>
            <span>Ваш пол:</span>
            <input type="radio" name="state" id="male" value="Мужской">
            <label for="male">Мужской</label>
            <input type="radio" name="state" id="female" value="Женский">
            <label for="female">Женский</label>
            <input type="radio" name="state" id="hz" value="Еще не понял">
            <label for="female">Еще не понял</label>*
            <?php
            if (trim($state) == "") {
                echo 'Выберите пол';
                $state = "";
            }
            ?>

        </p>

        <input type="submit" value="Отправить">
    </form>
    <div>
        <?php

        if (trim($name) == "" || trim($email) == "" || trim($site) == "" || trim($coment) == "" || trim($state) == "") {
        } else {
            echo ' <h3>Новый коментарий</h3>
            <div>
            <p>' . $name . '</p>
            <p>' . $email . '</p>
            <p>' . $site . '</p>
            <p>' . $coment . '</p>
            <p>' . $state . '</p>
            </div>';
        }
        ?>
    </div>
</body>

</html>