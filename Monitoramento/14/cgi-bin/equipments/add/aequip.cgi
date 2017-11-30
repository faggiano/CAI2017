#!/bin/bash
read EQUIP
echo "content-type: text/html"
echo
DET=$(echo $EQUIP | cut -d"&" -f1 | cut -d"=" -f2)
LOC=$(echo $EQUIP | cut -d"&" -f2 | cut -d"=" -f2)
USR=$(echo $EQUIP | cut -d"&" -f3 | cut -d"=" -f2)
IPA=$(echo $EQUIP | cut -d"&" -f4 | cut -d"=" -f2)
echo $DET;$LOC;$USR;$IPA >> ../db/equipments.csv
echo "<html>"
echo "	<head>"
echo "	</head>"
echo "	<body>"
echo "		<h2><center>Equipamento Cadastrado com Sucesso</center></h2>"
echo "		<a href='/var/www/html/menu-monitor/menum.html'>Clique aqui para retornar ao menu.</a>"
echo "	</body>"
echo "</html>"
