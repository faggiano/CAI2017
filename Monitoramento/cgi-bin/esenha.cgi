#!/bin/bash
read X
echo "content-type: text/html"
echo
echo "<html>"
echo "<head>"
echo "</head>"
echo "<body>"
USER=$(echo $X | cut -d"&" -f1 | cut -d"=" -f2)
EMAIL=$(echo $X | cut -d"&" -f2 | cut -d"=" -f2)

if [[ $USER == $(cat login.txt | grep "^$USER;" | cut -d";" -f1) ]]
then
	if [[ $EMAIL == $(cat login.txt | grep "^$USER;" | cut -d";" -f2) ]]
	then
		echo "<meta http-equiv="refresh" content=0;"url=../pages/login.html">"
		source enviar.cgi $USER
else
		echo "<script>alert('Usuário inválido');</script>"
		echo "<meta http-equiv="refresh" content=0;"url=../pages/login.html">"
fi
else 
		echo "<script>alert('Usuário inválido');</script>"
		echo "<meta http-equiv="refresh" content=0;"url=../pages/login.html">"
fi
echo "</body>"
echo "</html>"
