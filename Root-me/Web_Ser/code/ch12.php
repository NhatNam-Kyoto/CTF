<?php

$inc="accueil.php";
if (isset($_GET["inc"])) {
    $inc=$_GET['inc'];
    if (file_exists($inc)){
	$f=basename(realpath($inc));
	if ($f == "index.php" || $f == "ch12.php"){
	    $inc="accueil.php";
	}
    }
}

include("config.php");


echo '
  <html>
  <body>
    <h1>FileManager v 0.01</h1>
    <ul>
	<li><a href="?inc=accueil.php">home</a