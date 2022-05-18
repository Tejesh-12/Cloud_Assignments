<?php include "../inc/dbinfo.inc"; ?>

<?php
$data = $_POST['user'];
// Create connection
$conn = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

if(!TableExists("feedback", $conn, DB_DATABASE))
{
   $query = "CREATE TABLE feedback (
       Complaint VARCHAR(90)
     )";
if(!mysqli_query($conn, $query)) echo("<p>Error creating table.</p>");
}


function TableExists($tableName, $connection, $dbName) {
  $t = mysqli_real_escape_string($connection, $tableName);
  $d = mysqli_real_escape_string($connection, $dbName);

  $checktable = mysqli_query($connection,
      "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_NAME = '$t' AND TABLE_SCHEMA = '$d'");

  if(mysqli_num_rows($checktable) > 0) return true;

  return false;
}

$sql = "INSERT INTO feedback (feedback)
VALUES ('$data')";

if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?>
