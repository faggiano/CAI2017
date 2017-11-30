#!/bin/bash
read login
echo "content-type: text/html"
echo
echo "<html>"
echo "<head>"
echo "<meta charset='UTF-8'>"
echo "</head>"
USER=$(echo "$login" | cut -d"&" -f1 | cut -d"=" -f2)
PASS=$(echo "$login" | cut -d"&" -f2 | cut -d"=" -f2)
PASS=$(echo "$PASS" | sha256sum | cut -d" " -f1)
tipo=$(grep "$USER\;" login.txt | cut -d";" -f4)
echo "<body>"
if [[ $USER == $(cat login.txt | grep "^$USER;" | cut -d";" -f1) ]]
then
		if [[ $PASS == $(cat login.txt | grep "^$USER;" | cut -d";" -f3) ]]
		then
				if [[ $tipo == "tecnico" ]]
				then
					echo "<meta http-equiv="refresh" content=0;url="../index.html">"
				else
					echo "<meta http-equiv="refresh" content=0;url="../pages/comum.html">"
				fi
		else
			echo "<script>alert('Senha incorreta');</script>"
			echo "<meta http-equiv="refresh" content=0;url="../pages/login.html">"
		fi
else
	echo "<script>('Usuário não cadastrado');</script>"
	echo "<meta http-equiv="refresh" content=0;url="../pages/login.html">"
fi
echo "</body>"
echo "</html>"
