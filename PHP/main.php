<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div>
        <h1> Задание 1 </h1>
        <?php
        $name = "Павел";
        $surname = "Иванов";
        $date = 1;
        $month = 11;
        $year = 1999;
        $age = 20;
        $happy = 0.76;

        echo "Имя: $name, фамилия: $surname";
        echo "Дата рождения: $date $month $year";
        echo "Возраст: $age";
        echo "Уровень счастья: $happy";

        ?>
    </div>
    <div>
        <h1> Задание 2 </h1>
        <?php
        $hasCar = false;
        $number = -0.78902;
        echo "Есть машина? $hasCar";
        echo "Число - $number";
        ?>
        <br>
        <?php
        define("NUMBER_E", 2.71828);
        echo NUMBER_E;
        ?>
        <br>
        <?php
        echo defined("NUMBER_E");
        ?>
    </div>
    <div>
        <h1> Задание 3 | Математика </h1>

        <?php
        $x = 10;
        $y = 20;
        echo $x + $y . '<br>';
        echo $x - $y . '<br>';
        echo $x * $y . '<br>';
        echo $x / $y . '<br>';
        echo $x % $y . '<br>';
        $x += 10; // $x = $x + 10;
        $y -= 10; // $y = $y - 10;
        echo $x . '<br>';
        echo $y . '<br>';
        $x++; // $x += 1;
        $x--; // $x -= 1;
        echo M_PI . '<br>';
        echo M_E . '<br>';
        echo abs(-22) . '<br>';
        echo round(3.5556734, 2) . '<br>';
        $rand = mt_rand(1, 20);
        $rand++;
        echo $rand . '<br>';
        echo max(2, 5, 6, 1, 8, 3, 6) . '<br>';
        ?>
        <hr>
        <?php
        $first = 5.6;
        $second = 8.9;
        $summ = $first + $second;
        $diff = $first - $second;
        $mult = $first * $second;
        $divide = $first / $second;
        $ostatok = $first % $second;
        echo "Сумма: $summ";
        echo "Разница: $diff";
        echo "Умножение: $mult";
        echo "Деление: $divide";
        echo "Остаток: $ostatok";
        ?>
        <hr>
        <?php
        $a = -2;
        $a *= 3;
        $a++;
        echo "Результат: $a";
        ?>
        <hr>
        <?php
        echo "Максимум - " . max(9, 23, 0, -24.5, 34, 11, 41, 3, -3.2, 3);
        ?>
        <hr>
        <?php
        echo floor(sqrt(2));
        ?>
        <hr>
    </div>
    <div>
        <h1> Задание 4 | Строки </h1>
        <?php
        $str = "Hello";
        echo "VAR: $str" . '!';
        echo "<input type=\"text\"><br>";
        $length = strlen($str);
        echo strtoupper(trim(" some "));
        echo $length;
        echo md5("qwerty");
        ?>
        <hr>
        <?php
        echo "\"";
        echo " ' ";
        echo "\\";
        echo "\n";
        echo "<div>Просто блок</div>";
        echo '<hr>';
        echo "\"" . " ' " . "\\" . "\n" . "<div>Просто блок</div>";
        ?>
        <hr>
        <?php
        $string = "ASDПросто текстASD";
        // Первое задание
        $newStr = substr($string, 0, strlen($string) - 3); // Обрезаем все символы, кроме 3 последних
        echo "Обрезанная строка - $newStr";
        // Второе задание
        $lowerCase = substr($newStr, 0, 3);
        // Обрезанную часть в нижний регистр + добавляем прежнюю строку, но без первых трех элементов
        $result = strtolower($lowerCase);
        $result .= substr($newStr, 3, strlen($newStr));
        echo "Нижний регистр - $result";
        // Третье задание
        echo "Первые три символа - " . substr($result, 0, 3);
        ?>
        <hr>
    </div>
    <div>
        <h1>Задание 5 | Условные операторы</h1>
        <?php
        $a = 23;
        if ($a == 5)
            echo "10";
        else if ($a == 10)
            echo "15";
        else if ($a == 30)
            echo "20";
        else
            echo "Что-то не то!";
        ?>
        <hr>
        <?php
        $x = 15;
        $y = 5.6;
        echo $x == 15;
        echo $y >= 6;
        echo $x == $y;
        ?>
        <hr>
        <?php
        $a = 34;
        echo ($a < 50 && $a != 37 && $a >= 32) || ($a == 0 || $a == 15);
        ?>
        <hr>
        <?php
        $x = 7;
        $y = "7";
        $res = $x === $y;
        echo "$x === $y = $res";
        ?>
        <hr>

        <?php
        $a = 2;
        $b = 5;
        if ($a % 2 == 0)
            echo $b . ' - нечетное число';
        else
            echo $a . ' - нечетное число';
        ?>
        <hr>
        <?php
        $a = 5;
        $b = -3;
        $res = $b != 0 ? ($a / $b) : 1;
        echo "Результат: $res";
        ?>
        <hr>
    </div>
</body>

</html>