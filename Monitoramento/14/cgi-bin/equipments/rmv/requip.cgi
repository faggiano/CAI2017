#!/bin/bash
read EQUIP
echo "content-type: text/html"
echo
RMVEQUIP=$(echo $EQUIP | cut -d"=" -f2)
cp ../db/equipments.csv /usr/share/backup/equipments.csv.bkp
grep -v "\;$RMVEQUIP\;" ../db/equipments.csv > ../db/equipments.csv
echo "<html>"
echo "	<head>"
echo "	</head>"
echo "	<body>"
echo "	<h1>Equipamento Removido.</h1>"
echo "	<a href='../../../menu-monitor/menum.html'>Clique aqui para retornar ao menu.</a>"
echo "	</body>"
echo "</html>"
