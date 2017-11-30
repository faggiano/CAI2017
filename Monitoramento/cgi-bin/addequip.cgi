#!/bin/bash
read EQUIP
clear
echo "content-type: text/html"
echo
DESC=$(echo $EQUIP | cut -d"&" -f1 | cut -d"=" -f2)
USER=$(echo $EQUIP | cut -d"&" -f2 | cut -d"=" -f2)
LOC=$(echo $EQUIP | cut -d"&" -f3 | cut -d"=" -f2)
echo "$DESC;$USER;$LOC" >> equipments.csv &
if [[ $? == '0' ]] ; then
	echo "<h2>Equipamento adicionado com sucesso.</h2>"
	echo "<a href='./html/menum.html'>Clique aqui para retornar ao menu.</a>"
else
	echo "<h2>Ocorreu um erro na adição do equipamento.</h2>"
	echo "<a href='./equips.cgi'>Clique aqui para tentar novamente.</a>"
fi
