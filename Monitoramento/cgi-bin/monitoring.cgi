#!/bin/bash
read OPTION
clear
echo "content-type: text/html"
echo
echo "<!DOCTYPE html>"
echo "<html>"
echo	"<head>"
echo		"<style>"
echo			"table {"
echo				"font-family: arial, sans-serif;"
echo				"border-collapse: collapse;"
echo				"width: 100%;"
echo			"}"
echo			"td, th {"
echo				"border: 1px solid #dddddd;"
echo				"text-align: left;"
echo				"padding: 8px;"
echo			"}"
echo			"tr:nth-child(even) {"
echo				"background-color: #dddddd;"
echo			"}"
echo		"</style>"
echo 	"</head>"
echo 	"<body	onload='setInterval(function() {window.location.reload();}, 5000);'>"
echo 		"<table>"
echo 			"<tr>"
echo 				"<th>Description</th>"
echo    			"<th>User</th>"
echo    			"<th>Status</th>"
echo			"</tr>"
for x in $(cat .reports) ; do
	DESC=$(echo $x | cut -d";" -f1)
	USER=$(echo $x | cut -d";" -f2)
	STATS=$(echo $x | cut -d";" -f3)
	echo "<tr>"
	echo 	"<td>$DESC</td>"
	echo 	"<td>$USER</td>"
	echo 	"<td>$STATS</td>"
	echo "</tr>"
done
echo 		"</table>"
echo	"</body>"
echo "</html>
