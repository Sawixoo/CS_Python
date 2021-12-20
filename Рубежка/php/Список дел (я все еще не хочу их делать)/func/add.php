<?php
require_once 'connect.php';
$tasks = $_POST['tasks'];

mysqli_query($con, "INSERT INTO `task_list` (`id`, `actions`) VALUES (NULL,'$tasks') ");

header('Location: ../index.php');
