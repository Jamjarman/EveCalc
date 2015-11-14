<?php
$conLogin=mysqli_connect("localhost", "root", "fantasyFlight2", "EveCalcMaster");
if (mysqli_connect_errno()) {
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}


session_start();
$salt=mcrypt_create_iv(50, MCRYPT_DEV_URANDOM);

function printVar($var){
	echo '<br/>' . $var . '<br/>';
	print_r($var);
}


$username=$_GET['username'];
$password=$_GET['password'];
$apiKey=$_GET['api'];
$vCode=$_GET['vCode'];
$contactMethod=$_GET['contactMethod'];
$contactAddr=$_GET['contactAddress'];
$saltedPass=$password.$salt;
$hash=sha1($saltedPass);
$wallet=$_GET['wallet'];
$insertQuery="INSERT INTO `Requests` (`apiKey`, `vCode`, `username`, `salt`, `saltedPass`, `wallet`, `contactMethod`, `contactName`) VALUES ('".$apiKey."', '".$vCode."', '".$username."', '".$salt."', '".$hash."', '".$wallet."', '".$contactMethod."', '".$contactAddr."')";
mysqli_query($conLogin, $insertQuery);
		// Create connection
   
?>
<html>
</html>