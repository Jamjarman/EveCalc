<?php
$query="SELECT SUM(profit) AS totalProfit FROM Profit";
$queryResult=mysqli_query($con, $query);
$profit=mysqli_fetch_array($queryResult);
echo number_format($profit['totalProfit'], 2)." isk";
?>
