<?php
require_once 'func/connect.php';
$sql_select = mysqli_query($con, "SELECT * FROM `task_list`");
$sql_select = mysqli_fetch_all($sql_select);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>Список дел (Которые я не желаю делать)</h1>
    <form action="func/add.php" method="post">
        <label>
            <input type="text" name="tasks" placeholder="Сюда писать....">
            <input type="submit" value="Добавить">
        </label>
    </form>
    <table>
        <tr>
            <th>№</th>
            <th>Задание</th>
            <th>Действие</th>
        </tr>
        <?php
        foreach ($sql_select as $item) {
            echo '<tr> 
                <td>' . $item[0] . '</td> 
                <td>' . $item[1] . '</td> 
                <td> <a href="func/delete.php?id=' . $item[0] . '">Удалить</a></td> 
                </tr>';
        }

        ?>
    </table>

</body>

</html>