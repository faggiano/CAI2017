#!/bin/bash
cat <<FIMDOSCRIPT12321
content-type: text/html

<form action="opcao.cgi" method="post">
  <input type="radio" name="OPCAO" value="1" > Olá Mundo<br>
  <input type="radio" name="OPCAO" value="2" checked> Calculadora<br>
  <input type="radio" name="OPCAO" value="3"> Sair
  <br/>
  <input type="submit" value="Entrar">
</form>
FIMDOSCRIPT12321
