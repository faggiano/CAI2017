#!/bin/bash

PASSWD="/home/vagrant/CAI/ariels/passwd"

incorreto(){ dialog --msgbox "Login incorrect" 0 0 ; menu ; }
menu(){
		while : ;	do
		LOGIN=$(dialog --stdout --title "Login" --inputbox "jessie login:" 0 0)
		PASSW=$(dialog --stdout --title "Password" --passwordbox "Digite a sua senha:" 0 0)
		[[ $PASSW == "" ]] && incorreto
		[[ $LOGIN == "" ]] && incorreto
		PASSW=$(echo $PASSW | sha256sum | cut -d" " -f1)
		if [[ $(grep $LOGIN $PASSWD) ]] 
		then
			SENHA=$(grep $LOGIN $PASSWD | cut -d":" -f2)
			[[ $PASSW == $SENHA ]] && break || incorreto
		else
			incorreto
		fi
	done
}
menu
clear
