#!/bin/bash

incorreto(){  dialog --msgbox "Login incorrect" 0 0 ; }

menu(){
while : ; do
		
		
		LOGIN=$(dialog --stdout --title "Login" --inputbox "jessie login: " 0 0)
		PASSW=$(dialog --stdout --title "Password" --passwordbox "Digite a sua senha: " 0 0)
		
		#if [[ $LOGIN == "" ]]
			#then
			#dialog --title "ERRO!" --msgbox "Erro de usuário" 0 0
			#menu
			#exit 0
			#fi

		#[[ $LOGIN != " " ]] && 	PASSW=$(dialog --stdout --title "Password" --passwordbox "Digite a sua senha: " 0 0) ||
					#PASSW=$(dialog --stdout --title "Password" --passwordbox "Digite a sua senha: " 0 0)
	
	
	
		echo

		#PASSW=$(echo $PASSW | sha256sum | cut -d" " -f1 )	

		[[ -z $LOGIN ]]	&& incorreto
		[[ -z $PASSW ]] && incorreto
	
		PASSWD=/home/vinicius/CAI/CAI/viniciusb/passwd
		PASSW=$(echo $PASSW | sha256sum | cut -d" " -f1)
		
		if [[ $(grep $LOGIN $PASSWD) ]]
		then
			SENHA=$(grep $LOGIN $PASSWD | cut -d";" -f2) #f2 vai pegar no segundo campo
			 [[ $PASSW == $SENHA ]] && break 3 || incorreto
		
				else
					 incorreto
				fi						
done
}

menu
