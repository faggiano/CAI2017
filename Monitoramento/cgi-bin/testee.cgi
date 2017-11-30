#!/bin/bash
read X
echo "content-type: text/html"
echo
echo "<html>"
echo "<head>"
echo "<meta charset='UTF-8'>"
echo "</head>"
echo "<body>"
echo "<p>$X</p>"
echo "</body>"
echo "</html>"

