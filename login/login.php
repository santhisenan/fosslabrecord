<?php 
define('DB_SERVER','localhost');
define('DB_USERNAME','fc');
define('DB_PASSWORD','');
define('DB_DATABASE','fossdb');
$db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
$error="";
if($_SERVER["REQUEST_METHOD"] == "POST"){
	$myusername = mysqli_real_escape_string($db,$_POST['username']);
    $mypassword = mysqli_real_escape_string($db,$_POST['password']);
    $sql = "SELECT id FROM admin WHERE username = '$myusername' and password = '$mypassword'";
      $result = mysqli_query($db,$sql);
      $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
      $active = $row['active'];
      $count = mysqli_num_rows($result);
      if($count == 1) {
         header("location: welcome.php");
      }else {
        echo $result;
        $error = "Your Login Name or Password is invalid";
      }
}

 ?>

 <html>	
<head>
	<title>Login Page
	</title>
</head>

<body>
<div><?php echo $error ?></div>
	<form action="login.php" method="POST">
		<input type="text" placeholder="username" name="username">
		<input type="password" placeholder="password" name="password">
		<input type="submit" value="submit">

	</form>
</body>


 </html>