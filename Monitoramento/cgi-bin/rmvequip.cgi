#!/bin/bash
read EQUIP
clear
echo "content-type: text/html"
echo
echo "$EQUIP | grep -v equipments.csv" > equipments.csv
if [[ $? == '0' ]] ; then
	echo "<h2>Equipamento removido com sucesso</h2>"
	echo "<a href='../pages/menum.html'>Clique aqui para retornar ao menu.</a>"
else
	echo "<h2>Ocorreu um erro ao remover o equipamento.</h2>"
	echo "<a href='../pages/menum.html'>Clique aqui para tentar novamente.</a>"
fi
