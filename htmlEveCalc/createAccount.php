<!DOCTYPE html>
<html>
<head>
  <title>Statastic Login</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <link href="signin.css" rel="stylesheet"/>
</head>
<body>
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="js/bootstrap.min.js"></script>

  <div class="container">
    <center>
    	<form class="form-signin" role="form" action=newAccount.php>
    		<h1><small>Fill out the following forms to request a user account. Please user your eve characters first name for your username</small></h1>
    		<input type="username" class="form-control" name="username" placeholder="Username" required autofocus>
    		<input type="password" class="form-control" name="password" placeholder="Password" required>
		<input type="text" class="form-control" name="api" placeholder="API Key" required>
		<input type="text" class="form-control" name="vCode" placeholder="V Code" required>
		<h2><small>What number wallet do you use to buy raw materials? Please use the form 100# Where # is the number of the wallet given Master wallet is 0</small></h2>
		<input type="text" class="form-control" name="wallet" placeholder="Wallet Number" required>
		<h2><small>What is the best method to contact you? Please include the contact info for said method</small></h2>
		<input type="radio" name="contactMethod" value="reddit">Reddit</br>
		<input type="radio" name="contactMethod" value="email">Email</br>
		<input type="text" class="form-control" name="contactAddress" placeholder="Contact Address" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Submit</button>
    </br>
</form>
</center>
</html>
