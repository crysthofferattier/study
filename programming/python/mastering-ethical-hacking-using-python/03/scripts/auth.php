<?php

$username = $_POST['username'];
$password = $_POST['password'];

if ($username == "askar" && $password == '123456') {
    echo "Login Success!"
} else {
    echo "Login Failed!"
}

?>