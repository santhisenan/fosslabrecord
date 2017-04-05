<?php 
include("config.php");
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
	<form action="" method="POST">
		<input type="text" placeholder="username" name="username">
		<input type="password" placeholder="password" name="password">
		<input type="submit" value="submit">

	</form>
</body>


 </html>