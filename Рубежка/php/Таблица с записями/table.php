<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table</title>
</head>

<body>
    <?php
    $conn = new mysqli("localhost", "root", "root", "users");
    if ($conn->connect_error) {
        die("Ошибка: " . $conn->connect_error);
    }
    $sql = "SELECT * FROM person";
    if ($result = $conn->query($sql)) {
        echo "<table><tr><th>Id</th><th>Имя</th><th>Фамилия</th></tr>";
        foreach ($result as $row) {
            echo "<tr>";
            echo "<td>" . $row["id"] . "</td>";
            echo "<td>" . $row["name"] . "</td>";
            echo "<td>" . $row["surname"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
        $result->free();
    } else {
        echo "Ошибка: " . $conn->error;
    }
    $conn->close();

    ?>
</body>

</html>