<?php
    $servername ="localhost";
    $username   = "root";
    $password   = "";
    $dbname     = "myDB";
    $conn = mysqli_connect($servername, $username, $password, $dbname);
    if($conn)
    {
        echo "Connection ok";
    }
    else
    {
        echo "Connection failed";
    }
?>