#!/bin/bash
read TESTE
passou(){
VAR='<html>
<h1>Parabéns, você passou!</h1>
</html>'
}
naopassou(){
VAR='
<html>
<h1>PQP, você errou!</h1>
	<a href="../index2.html">
		<h4>Clica aqui pra voltar pro login...</h4>
	</a>
</html>'
}
USUARIO=$(echo $TESTE | cut -d"&" -f1 | cut -d"=" -f2)
SENHA=$(echo $TESTE | cut -d"&" -f2 | cut -d"=" -f2)
[[ $USUARIO == "vagrant" ]] && [[ $SENHA == "vagrant" ]] && \
passou || naopassou

echo "Content-type: text/html"
echo 
echo $VAR


