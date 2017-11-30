#!/bin/bash
read OPTION
echo "content-type: text/html"
echo
echo $OPTION > teste.txt
okayokay(){
	echo "<html><body><h2>Serviço executado com sucesso.</h2><a href='./html/menum.html'>Clique aqui para voltar ao menu.</a>"
}
wrongwrong(){
	echo "<html><body><h2>Ocorreu um erro no comando.</h2><a href='./html/menum.html'>Clique aqui para voltar ao menu.</a>"
}
startping(){
	source "./pingbreak.cgi 'start'"
	[[ $? == '0' ]] && okayokay || wrongwrong
}
stopping(){
	source "./pingbreak.cgi 'stop'"
	[[ $? == '0' ]] && okayokay || wrongwrong
}
equipments(){ 
	source ./html/equip.html
}
case $OPTION in
	"launchserv") startping ;;
	"ceaseserv") stopping ;;
	"equip") equipments ;;
	"return") source ../menum.html ;;
	*) echo "<h1><center>Erro. Opção Inválida.</center></h1><a href='../menum.html'>Clique aqui para voltar ao menu.</a>"
esac
