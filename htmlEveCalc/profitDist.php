<?php
$allTimeQueryProfit="SELECT SUM(profit) AS totalProfit FROM Profit";
$queryResult=mysqli_query($con, $allTimeQueryProfit);
$profit=mysqli_fetch_array($queryResult);
echo "<table class=\"table table-striped\"><thead><tr><th>Timeframe</th><th>PLEX</th><th>Ships</td></tr></thead><tbody><tr><td>All Time</td><td>";
echo number_format($profit['totalProfit']*.3, 2)." isk</td><td>".number_format($profit['totalProfit']*.2, 2)." isk</td></tr><tr><td>This Month</td><td>";
$thisMonthQuery="SELECT SUM(profit) as totalProfit FROM Profit WHERE MONTH(timestamp)=MONTH(CURDATE())";
$monthResult=mysqli_query($con, $thisMonthQuery);
$monthProfit=mysqli_fetch_array($monthResult);
echo number_format($monthProfit['totalProfit']*.3, 2)." isk</td><td>".number_format($monthProfit['totalProfit']*.2, 2)." isk</td></tr><tr><td>This Week</td><td>";
$thisWeekQuery="SELECT SUM(profit) as totalProfit FROM Profit WHERE WEEK(timestamp)=WEEK(CURDATE())";
$weekResult=mysqli_query($con, $thisWeekQuery);
$weekProfit=mysqli_fetch_array($weekResult);
echo number_format($weekProfit['totalProfit']*.3, 2)." isk</td><td>".number_format($weekProfit['totalProfit']*.2, 2)." isk</td></tr><tr><td>Today</td><td>";
$thisDayQuery="SELECT SUM(profit) as totalProfit FROM Profit WHERE DAY(timestamp)=DAY(CURDATE())";
$dayResult=mysqli_query($con, $thisDayQuery);
$dayProfit=mysqli_fetch_array($dayResult);
echo number_format($dayProfit['totalProfit']*.3, 2)." isk</td><td>".number_format($dayProfit['totalProfit']*.2, 2)." isk</td></tr></tbody></table>";
?>