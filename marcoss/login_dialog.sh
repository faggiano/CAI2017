#!/bin/bash
PASSWD="/home/vagrant/CAI/marcoss/passwd"
incorreto(){ dialog --msgbox "Login incorrect" 0 0 ; menu; }
menu(){
	LOGIN=$(dialog --stdout --title "Login" \
	--inputbox "Digite o seu usuário:" 0 0)
	PASSW=$(dialog --stdout --title "Password" \
	--passwordbox "Digite a sua senha:" 0 0)
	PASSW=$(echo $PASSW | sha256sum | cut -d" " -f1)
	if [[ $LOGIN == "" ]] || [[ $PASSW == "" ]]; then
		incorreto
	else
		if [[ $(grep $LOGIN $PASSWD) ]]; then
				SENHA=$(grep $LOGIN $PASSWD | cut -d";" -f2)
				[[ $PASSW == $SENHA ]] && (clear ; exit 0) || incorreto
		else
			incorreto
		fi
	fi
	clear
}
menu
