#!/bin/bash
read TESTE
passou(){
	VAR=' <html><h1>Parábens, você passou!</h1></html> '
}
naopassou(){
	VAR=' <html><h1>Você errou!</h1><a href="../index2.html"><h4>Clique aqui para voltar para o login</h4></html> '
}
USUARIO=$(echo $TESTE | cut -d"&" -f1 | cut -d"=" -f2)
SENHA=$(echo $TESTE | cut -d"&" -f2 | cut -d"=" -f2)
[[ $USUARIO == "vagrant" ]] && [[ $SENHA == "vagrant" ]] && passou || naopassou

echo "content-type: text/html"
echo
echo $VAR
