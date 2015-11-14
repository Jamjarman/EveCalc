<?php
$query="SELECT * FROM `Inventory` WHERE 1 ORDER BY ID ASC";
if(!empty($_POST['item'])){
  $itemName=$_POST['item'];
  $query="SELECT * FROM `Inventory` WHERE `itemName`=\"".$itemName."\" ORDER BY ID ASC";
}
$queryResult=mysqli_query($con, $query);
echo "<table class=\"table table-striped\"><thead><tr><th>Item</th><th>Buy Price</th><th>Quantity</th><th>Timestamp</th></tr></thead><tbody>";
while($row=mysqli_fetch_array($queryResult)){
  echo "<tr><td>".$row['itemName']."</td><td>".number_format($row['price'], 2)."</td><td>".number_format($row['quantity'], 0)."</td><td>".$row['acquired']."</td></tr>";
}
echo "</tbody></table>";
?>
<html></html>