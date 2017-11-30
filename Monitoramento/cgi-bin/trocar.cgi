#!/bin/bash
read X
USER=$(echo $X | cut -d"&" -f1 | cut -d"=" -f2)
PASS=$(echo $X | cut -d"&" -f2 | cut -d"=" -f2)
PASS2=$(echo $X | cut -d"&" -f3 | cut -d"=" -f2)
echo "content-type: text/html"
echo
if [[ $PASS == $PASS2 ]]
	then 
	echo "<meta http-equiv="refresh" content=1;"url=../index.html">"
	PASS=$(echo $PASS2 | sha256sum | cut -d" " -f1)
	linha=$(grep ^$USER\; 'login.txt')
	var2=$(echo $linha | cut -d";" -f3)
	echo $linha | sed s/$var2/$PASS/g >> 'arquivo2.pwd'
	sed /$linha/d 'arquivo2.pwd' > 'login.txt'
else
	echo "<meta http-equiv="refresh" content=1;"url=../trocar.html">"
echo "<h1>Senhas inválidas</h1>"
fi
	
