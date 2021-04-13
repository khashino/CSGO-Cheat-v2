<?php
	include_once('config.php');
	$username = isset($_GET['username']) ? mysqli_real_escape_string($conn, $_GET['username']) :  "";
	$password = isset($_GET['password']) ? mysqli_real_escape_string($conn, $_GET['password']) :  "";
	$sql = "SELECT * FROM `khashaya_test`.`users` WHERE username='{$username}' and password='{$password}';";
	$get_data_query = mysqli_query($conn, $sql) or die(mysqli_error($conn));
		if(mysqli_num_rows($get_data_query)!=0){
		$result = array();

		while($r = mysqli_fetch_array($get_data_query)){
			extract($r);
			$result[] = array("isactive" => $isactive, "isadmin" => $isadmin);
		}
		$json = array("status" => 1, "info" => $result);
		//$json = $result
	}
	else{
		$json = array("status" => 0, "info" => "user not found");
	}

@mysqli_close($conn);
// Set Content-type to JSON
header('Content-type: application/json');
echo json_encode($json);