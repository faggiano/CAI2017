#!/bin/bash
read OPTION
clear
echo "content-type: text/html"
echo
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
for x in $(cat ../report/reports) ; do
	echo "<tr>"
	for y in $(echo $x) ; do
		echo 	"<td>$(echo $y | cut -d";" -f1)</td>"
		echo 	"<td>$(echo $y | cut -d";" -f2)</td>"
		echo 	"<td>$(echo $y | cut -d";" -f3)</td>"
	done
	echo "</tr>"
done
echo 		"</table>"
echo	"</body>"
echo "</html>
