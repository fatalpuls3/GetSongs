<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>iLLER J Music Search</title>
	<meta name="keywords" content="" />
	<meta name="description" content="" />
	<link href="style.css" rel="stylesheet" type="text/css" media="screen" />
	<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
	<link rel="icon" href="/favicon.ico" type="image/x-icon">
</head>
<body>
<center>
<h1></h1>
	<img src=".\images\logo2.png" width = "10%" height = "10%">
	<p>
	<form action="" method="get">
		<input type="text" name="search" value=""/>
		<select name="tag">
			<option value = "artist">Artist</option>
			<option value = "album">Album</option>
			<option value = "genre">Genre</option>
			<option value = "title">Song Title</option>
		</select>
		<input type="submit" name="submit" value="Search"/>
		<a href="index.php">Clear</a>
	</form>
	</form>
<h1></h1>
	<p>
	<a href="Recently <font color = white>Recently Added Songs</font>
	<div id="results">
		<?php
		$conn = new PDO('sqlite:song_db.db'); 
		require_once 'Pager/Pager.php';
		isset($_REQUEST['search']) ? $search = $_REQUEST['search'] : $search = "";
		isset($_REQUEST['tag']) ? $tag = $_REQUEST['tag'] : $tag = "";
		$count = 0;
		
		If(!empty($search))
		{
			/* First we need to get the total rows in the table */			
			$qry = "SELECT * FROM songs WHERE ".$tag." LIKE '%".$search."%'";
			$result = $conn->query($qry);
			if($result === false) {
				print_r($conn->errorInfo());
			}
			$totrows = count($result->fetchall());
			$pager_options = array(
				'mode'       => 'Jumping',
				'perPage'    => 20,
				'delta'      => 5,
				'separator' => '-',
				'totalItems' => $totrows,
			);
			$pager = Pager::factory($pager_options);
			list($from, $to) = $pager->getOffsetByPageId();
			$from = $from - 1;
			$perPage = $pager_options['perPage'];
			$query = $conn->query( "SELECT * FROM songs WHERE ".$tag." LIKE '%".$search."%'  LIMIT ".$from." , ".$perPage.""); // buffered result set
			echo '<table id="searchresults" class="clearfix">';
			
			if($totrows > 0)
			{
				echo "<tr><th>Artists</th><th>Album</th><th>Song Title</th><th>Folder</th><td>Path</th></tr>";
				foreach($query as $entry)
				{
					echo "<tr><td>".$entry['artist']."</td><td align=center>".$entry['album']."</td><td>".$entry['title']."</td><td align=left>".$entry['genre']."</td><td align=left><a href=".$entry['filepath'].">path</a></td></tr>";
				}
			echo '</table>';
			} else {
				echo '<font size = 4, font color  = #ffffff>Sorry there were no search results found please try another keyword or phrase</font>';
			}

			if(isset($pager))
			{
				echo '<div class="pager">';
				echo $pager->links;
				echo '</div>';
			}
		}
		?>
	</div>
</center>