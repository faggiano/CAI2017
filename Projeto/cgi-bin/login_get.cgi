#!/bin/bash
#QUERY_STRING="USER=evelyn&PASS=thales"
USER=$(echo $QUERY_STRING | cut -d"&" -f1 | cut -d"=" -f2)
PASS=$(echo $QUERY_STRING | cut -d"&" -f2 | cut -d"=" -f2)
echo content-type: text/html
echo
if [[ $USER == "evelyn" ]]
then
	if [[ $PASS == "thales" ]]
	then
		echo "<h1>Logado!</h1>"
	else
		echo "<h1>Falhou!</h1>"
	fi
else
	echo "<h1>Falhou</h1>"
fi
