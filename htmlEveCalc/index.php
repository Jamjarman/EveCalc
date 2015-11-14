<?php
include 'includes.php';
?>
<!Doctype HTML>
<html>
<head>
	<title>Home</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
</head>
<body>
	<div class="container">
		<div class="navbar navbar-dafault navbar-fixed-top" role="navigation">
			<div class="container">
				<div class="navbar-header">
       				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
           				<span class="sr-only">Toggle navigation</span>
           				<span class="icon-bar"></span>
          			</button>
          			<a class="navbar-brand" href="explanation.html">Statastic</a>
          		</div>
          		<div class="navbar-collapse collapse">
          				<ul class="nav navbar-nav">
            				<li><a href="index.php">Home</a></li>
            				<li><a href="projects.php">Projects</a></li>
            				<li><a href="stats.php">Statistics</a></li>
            				<li><a href="newProj.php">New Project</a><li>
            				<li><a href="account.php">Account Management</a></li>
          				</ul>
        			</div><!--/.nav-collapse -->
			</div 
		</div>
	</div>
</br>
</br>
</br>
	<div class="hero-unit">
		Welcome to the Statastic homepage, trackier than the NSA!
	</div>
	<div class="row">
		<div class="col-md-10">
			<div class="container"><?php require 'simpleProject.php'; ?></div>
		</div>
		<div class="col-md-2">
			<div class="container">
				<ul>
					<li>Sample news item</li>
					<li>This is a real thing</li>
					<li>NEEEEWWWWS</li>
					<li>Expected release date: Stop rushing us</li>
				</ul>
			</div>
		</div>
	</div>
	 <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
</body>
</html>