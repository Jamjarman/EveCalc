<?php
session_start();
//printVar($_SESSION);
//printVar($_SESSION['permit']);
$_SESSION['permit']=0;
$_SESSION['user']="";
//printVar($_SESSION['permit']);
header("Location: index.html");
die();

function printVar($var){
	echo '<br/>' . $var . '<br/>';
	print_r($var);
}
?>
