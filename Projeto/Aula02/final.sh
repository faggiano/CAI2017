#!/bin/bash
PASSWD="/home/vagrant/Projeto/Aula02/passwd" # Local do arquivo
incorreto(){ sleep 3 ; echo ; echo "Login incorrect" ; } # Criou funçao
while : ; do #Primeiro Ciclo
	clear #Apaga Tela
	echo  #Pula linha
	echo "Debian GNU/Linux 8 jessie tty1" #Escreve texto
	echo #Pula Linha
	contar=0 #Cria variavel com valor igual a zero
	while : ;	do #Segundo Ciclo
		read -p "jessie login: " LOGIN #Imprime e salva o que o user digitar
		read -s -p "Password: " PASSW ##A mesma coisa com opção SECRET
		echo #Pula Linha
		if [[ -z $LOGIN || -z $PASSW || ! $(grep $LOGIN $PASSWD) ]] 
		then #Verifica se LOGIN e PASSW estao vazios assim se o GREP funciona
			incorreto #Se verdadeiro chama a função
		else #Caso contrario cria duas variaveis
			PASSW=$(echo $PASSW | sha256sum | cut -d" " -f1)
			SENHA=$(grep $LOGIN $PASSWD | cut -d";" -f2)
			[[ $PASSW == $SENHA ]] && break 2 || incorreto # Se acertar sai.
		fi
		contar=$(($contar+1)) #Modifica variável somando 1
		[[ $contar == "5" ]] && break #Se realizou 5 ciclos volta pro anterior
	done #Sai do segundo ciclo
done #Sai do primeiro ciclo
