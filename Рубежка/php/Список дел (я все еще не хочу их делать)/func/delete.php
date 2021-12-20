<?php
require_once 'connect.php';
$task_id = $_GET['id'];


mysqli_query($con, "DELETE FROM `task_list` WHERE `task_list`.`id` = '$task_id'");

header('Location: ../index.php');
