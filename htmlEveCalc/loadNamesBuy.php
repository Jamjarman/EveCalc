<?php
$query="SELECT DISTINCT itemName FROM `".$_POST['tableName']."` WHERE 1";
echo $query;
$queryResult=mysqli_query($con, $query);
while($row=mysqli_fetch_array($queryResult)){
  echo "<option value=\"".$row['itemName']."\">";
}
?>