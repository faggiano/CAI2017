#!/bin/bash

cat <<TRANQUEIRAAAA
content-type: text/html

<html>

<form action="operacao.cgi" method="post">
	Número A:
	<input type="text" name="NUMEROA">
	<br/>
	Número B:
	<input type="text" name="NUMEROB">
	<br/><br/>
	SOMA
	<input type="radio" name="OPERACAO" value="soma" >
	<br>
	SUBTRACAO	
	<input type="radio" name="OPERACAO" value="subtracao" >
	<br>
	MULTIPLICACAO
	<input type="radio" name="OPERACAO" value="multiplicacao" >
	<br>
	DIVISAO
	<input type="radio" name="OPERACAO" value="divisao" >
	<br>
	<input type="submit" value="Enviar">
</form>

</html>
TRANQUEIRAAAA
