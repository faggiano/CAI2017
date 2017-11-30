#!/bin/bash
read EQUIP
echo "content-type: text/html"
echo
echo "<html>"
RMVEQUIP=$(echo $EQUIP | cut -d"=" -f2)
grep "\;$RMVEQUIP\;" equipments.csv > equipments.csv.bkp
grep -v "\;$RMVEQUIP\;" equipments.csv.bkp > equipments.csv
echo "	<head>"
echo "	</head>"
echo "	<body>"
echo "	<h1>Equipamento Removido.</h1>"
echo "	<a href='../pages/menum.html'>Clique aqui para retornar ao menu.</a>"
echo "	</body>"
echo "</html>"
