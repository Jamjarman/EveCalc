<?php
$query="SELECT * FROM `Profit` WHERE 1 ORDER BY ID DESC";
if(!empty($_POST['item'])){
  $itemName=$_POST['item'];
  $query="SELECT * FROM `Profit` WHERE `itemName`=\"".$itemName."\" ORDER BY ID DESC";
}
$queryResult=mysqli_query($con, $query);
echo "<table class=\"table table-striped\"><thead><tr><th>Item</th><th>Buy Price</th><th>Sell Price</th><th>Quantity</th><th>Profit</th><th>Timestamp</th></tr></thead><tbody>";
while($row=mysqli_fetch_array($queryResult)){
  echo "<tr><td>".$row['itemName']."</td><td>".number_format($row['buyPrice'], 2)."</td><td>".number_format($row['sellPrice'], 2)."</td><td>".number_format($row['quantity'], 0)."</td><td>".number_format($row['profit'], 2)."</td><td>".$row['timestamp']."</td></tr>";
}
echo "</tbody></table>";
?>
<html></html>