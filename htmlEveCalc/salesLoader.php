<?php
$query="SELECT * FROM `SellHistory` WHERE 1 ORDER BY transactionID DESC";
if(!empty($_POST['item'])){
  $itemName=$_POST['item'];
  $query="SELECT * FROM `SellHistory` WHERE `itemName`=\"".$itemName."\" ORDER BY transactionID DESC";
}
$queryResult=mysqli_query($con, $query);
echo "<table class=\"table table-striped\"><thead><tr><th>Item</th><th>Sell Price</th><th>Quantity</th><th>Station</th><th>Timestamp</th></tr></thead><tbody>";
while($row=mysqli_fetch_array($queryResult)){
  echo "<tr><td>".$row['itemName']."</td><td>".number_format($row['price'], 2)."</td><td>".number_format($row['quantity'], 0)."</td><td>".$row['stationName']."</td><td>".$row['timestamp']."</td></tr>";
}
echo "</tbody></table>";
?>
<html></html>