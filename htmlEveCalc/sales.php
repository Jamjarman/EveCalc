<?php include 'includes.php'; ?>
<!Doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Home</title>
    <!--Stylesheets-->
    <link rel="stylesheet" href="bootstrap/css/bootstrap.css">
    <link rel="stylesheet" href="bootstrap/css/bootstrap-theme.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
</head>
<body>
  <!--Navbar-->
  <div class="navbar navbar-inverse navbar-static-top">
    <div class="navbar-inner">
      <div class="container">
	<div class="navbar-header">
	<button class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="true" aria-controls="navbar">
	  <span class="sr-only">Toggle Navigation</span>
	  <span class="icon-bar"></span>
	  <span class="icon-bar"></span>
	  <span class="icon-bar"></span>
	</button>
	<a class="navbar-brand" href="#">EveCalc</a>
	</div>
	<div id="navbar" class="navbar-collapse collapse">
	  <ul class="nav navbar-nav">
	    <li><a href="home.php">Home</a></li>
	    <li><a href="profit.php">Profit</a></li>
	    <li><a href="inventory.php">Inventory</a></li>
	    <li class="active"><a href="sales.php">Sales</a></li>
	    <li><a href="buy.php">Purchases</a></li>
	  </ul>
	</div>
      </div>
   </div>
 </div>
  <div class="container">
    <div class="row">
      <div class="col-md-2">
	<form class="form" action="sales.php">
	   <input type="text" class="form-control" list="datalistNames" name="item" placeholder="Item Name">
	  <datalist id="datalistNames">
	    <?php $_POST['tableName']="SaleHistory"; include 'loadNamesBuy.php';?>
	  </datalist>

	  </br>
	  <button type="submit" class="btn">Submit</button>
	</form>
</br>
	<form class="form" action="sales.php">
	  <button type="submit" class="btn">Clear</button>
	</form>
      </div>
      <div class="col-md-10">
	<?php if(!empty($_GET)){$_POST['item']=$_GET['item'];}  include 'salesLoader.php';?>
      </div>
    </div>
  </div>


  <!--Javascript-->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="bootstrap/js/bootstrap.min.js"></script>
</body>
</html>
