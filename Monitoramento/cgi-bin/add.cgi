#!/bin/bash
read X
echo "content-type: text/html"
echo
echo "<html>"
echo "<title>CADASTRO</title>"
echo "<head>"
echo "<meta charset='UTF-8'>"
echo "</head>"
echo "<body>"
TIPO=$(echo "$X" | cut -d"&" -f1 | cut -d"=" -f2)
USER=$(echo "$X" | cut -d"&" -f2 | cut -d"=" -f2)
EMAIL=$(echo "$X" | cut -d"&" -f3 | cut -d"=" -f2)
EMAIL2=$(echo "$X" | cut -d"&" -f4 | cut -d"=" -f2)
PASS=$(echo "$X" | cut -d"&" -f5 | cut -d"=" -f2)
PASS2=$(echo "$X" | cut -d"&" -f6 | cut -d"=" -f2)
if [[ $USER != $(cat login.txt | grep "^$USER\;" | cut -d";" -f1) ]]
then
if [[ $EMAIL == $EMAIL2 ]]
then
if [[ $PASS == $PASS2 ]]
then
EMAIL=$EMAIL
PASS=$(echo $PASS | sha256sum | cut -d" " -f1) 
echo "<meta http-equiv="refresh" content=1;"url=../pages/login.html">"
echo "$USER;$EMAIL;$PASS;$TIPO" >> login.txt
echo "<h1>Usuário cadastrado com sucesso</h1>"
else
echo "<meta http-equiv="refresh" content=2;"url=../pages/cadastro.html">"
echo "<p><center>Senhas Inválidas</center></p>"
fi
else
echo "<meta http-equiv="refresh" content=2;"url=../pages/cadastro.html">"
echo "<p><center>Emails inválidos</center></p>"
fi
else
echo "<meta http-equiv="refresh" content=2;"url=../pages/cadastro.html">"
echo "<h1>Usuário ja cadastrado!</h1>"
fi
echo "</body>"
echo "</html>"

