<?php
$conLogin=mysqli_connect("localhost", "root", "password", "EveCalcMaster");
if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}


session_start();
function printVar($var){
    echo '<br/>' . $var . '<br/>';
    print_r($var);
}

$user=$_GET['username'];
$pass=$_GET['password'];
$userQuery="SELECT * From Users WHERE username=\"".$user."\"";
    //printVar($userQuery);
$userRes=mysqli_query($conLogin, $userQuery);
$salt=array();
$saltedPass=array();
while($row=mysqli_fetch_array($userRes)){
        //printVar($row);
    $salt=$row['salt'];
    $saltedPass=$row['saltedPass'];
}
    //printVar($salt);
$newSaltPass=$pass.$salt;
    //printVar($newSaltPass);
$hashedPass=sha1($newSaltPass);
    //printVar($hashedPass);
    //printVar($saltedPass);
if($hashedPass==$saltedPass){
        //printVar("Good pass");
    $_SESSION['permit']=1;
    $_SESSION['user']=$user;
        //printVar($_SESSION['permit']);
        //printvar($_SESSION['user']);
    header("Location: home.php");
    die();
}
else{
    //printVar("Bad pass");
    header("Location: index.html");
    die();
}
?>

<html>
<head>
    <title>Sign In/title>
    </head>
    </html>