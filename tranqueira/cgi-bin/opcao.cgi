#!/bin/bash
read OPCAO
OPCAO=$(echo $OPCAO | cut -d"=" -f2)
case $OPCAO in
	1) . olamundo.cgi ;;
	2) . calculadora.cgi ;;
	3) . sair.cgi ;;
	*) . falhou.cgi ;;
esac
