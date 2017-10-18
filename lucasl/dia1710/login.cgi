#!/bin/bash
echo "content-type: text/html"
echo
echo"<h1>"
GERAL=$QUERY_STRING
NNOME=$(echo $GERAL | cut -d"&" -f1 | cut -d"=" -f2)
SSENHA=$(echo $GERAL | cut -d"&" -f2 | cut -d"=" -f2)
echo "A variável 'nnome' é igual a $NNOME<br/>"
echo "A variável 'ssenha' é igual a $SSENHA"
echo "</h1>"
