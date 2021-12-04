<?php


if (isset($_POST['submit'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    $mailto = "bioequizon@gmail.com";

 $headers = "From: ".$email;
 $txt = "You have received an e-mail from ".$name.".\n\n".$message;
 mail($mailto, $name, $txt, $headers);

 header("Location: index.php?mailsend");
 




?>