<!DOCTYPE HTML>
<head>
<title>Thank you for registering your Pizza Button</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<link rel="stylesheet" href="style.css" />
<head>
<body>
 <style type="text/css">
.tg  {text-align:center; }
.tg  {margin: 0 auto;}
.tg-031e {
    border-radius: 25px;
    border: 2px solid #33CCFF;
    padding: 20px; 
    width: 200px;
    height: 50px; 
}
</style>
<?php
$export_text="<ACTIVATION>\n";
$export_text=$export_text . "<first_name>" . $_POST["first_name"]. "</first_name>\n";
$export_text=$export_text . "<last_name>" . $_POST["last_name"]. "</last_name>\n";
$export_text=$export_text . "<address>" . $_POST["address"]. "</address>\n";
$export_text=$export_text . "<instructions>".$_POST["instructions"]."</instructions>";
$export_text=$export_text . "<email>" . $_POST["email"]. "</email>\n";
$export_text=$export_text . "<zip>" . $_POST["zip"]. "</zip>\n";
$export_text=$export_text . "<phone_number>" . $_POST["phone_number"]. "</phone_number>\n";
$export_text=$export_text . "<twitter>" . $_POST["twitter"]. "</twitter>\n";

//Credit Card info (encrypt)
$export_text=$export_text . "<billing_address>" . $_POST["billing_address"]. "</billing_address>\n";
$export_text=$export_text . "<billing_city>" . $_POST["billing_city"]. "</billing_city>\n";
$export_text=$export_text . "<billing_zip>" . $_POST["billing_zip"]. "</billing_zip>\n";
$export_text=$export_text . "<cc_number>" . $_POST["cc_number"]. "</cc_number>\n";
$export_text=$export_text . "<cc_type>" . $_POST["cc_type"]. "</cc_type>\n";
$export_text=$export_text . "<cc_expM>" . $_POST["cc_expM"]. "</cc_expM>\n";
$export_text=$export_text . "<cc_expY>" . $_POST["cc_expY"]. "</cc_expY>\n";
$export_text=$export_text . "<cc_sec>" . $_POST["cc_sec"]. "</cc_sec>\n";
$export_text=$export_text . "</ACTIVATION>";




file_put_contents ( "ACT_".substr($_POST["serial"],4,8), $export_text );
echo "<table><tr><td class=\"tg-031e\" ><center style=\"font-size:25px\">Thank you for registering your Pizza Button!<br>";
echo "To activate, please press the big red button now</center></td></tr></table>";
?>