<?php
// Create connection

		$con=mysqli_connect("localhost","root","password",$_SESSION['user']."EveCalc");
	

      // Check connection
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	//echo "connection successful";

	session_start();

      function printVar($var){
    	echo '<br/>' . $var . '<br/>';
    	print_r($var);
}

?>