
<?php include "../inc/dbinfo.inc"; ?>
<?php


// Create connection
$conn = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT * FROM feedback";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
  // output data of each row
  while($row = mysqli_fetch_assoc($result)) {
    echo "<h1>Complaint :" . $row["Complaint"]."</h1><br>";
  }
} else {
  echo "0 results";
}

mysqli_close($conn);
?>
