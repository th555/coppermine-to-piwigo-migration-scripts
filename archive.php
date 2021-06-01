<?php

define('IN_COPPERMINE', true);
define('THUMBNAILS_PHP', true);
define('INDEX_PHP', true);

require('include/init.inc.php');
include('include/archive.php');

$categories = cpg_db_fetch_rowset(
cpg_db_query("SELECT cid, name FROM {$CONFIG['TABLE_CATEGORIES']}"));

$fn = "./photopaths.csv";
file_put_contents($fn, "");

$outpt = "";

foreach ($categories as $row) {
    $cat_id = $row['cid'];
    $cat_name = $row['name'];
    $albums = cpg_db_fetch_rowset(
    cpg_db_query("SELECT aid, title FROM {$CONFIG['TABLE_ALBUMS']} WHERE category = $cat_id"));
    foreach ($albums as $roww) {
        $alb_id = $roww['aid'];
        $alb_name = $roww['title'];
        $pictures = cpg_db_fetch_rowset(cpg_db_query(
        "SELECT filepath, filename FROM {$CONFIG['TABLE_PICTURES']} WHERE aid = $alb_id"));
        foreach ($pictures as $rowww) {
            $path = $rowww['filepath'];
            $filename = $rowww['filename'];
            $outpt = "$cat_name;;$alb_name;;$path$filename\n";
            file_put_contents($fn, $outpt, FILE_APPEND);
        }
    }
}


?>
