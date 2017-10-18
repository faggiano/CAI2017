#!/bin/bash
PASSWD="/home/vagrant/pham/CAI/nhatp/passwd"
incorreto(){ sleep 3 ; dialog --msgbox "Login incorrect" 0 0; autentica ; }
autentica(){
while : ; do
		LOGIN=$(dialog --stdout --title "Login" \
    --inputbox  "jessie login: " 0 0)
	  PASSW=$(dialog --stdout --title "Password" \
		--passwordbox "Digite a sua senha" 0 0)
		[[ -z $LOGIN ]] && incorreto
		[[ -z $PASSW ]] && incorreto
		PASSW=$(echo $PASSW | sha256sum | cut -d" " -f1)
	if [[ $(grep $LOGIN $PASSWD) ]] 
	then
		SENHA=$(grep $LOGIN $PASSWD | cut -d";" -f2)   
	  [[ $PASSW == $SENHA ]] && break 3 || incorreto
		else
			incorreto
		fi
	done 
}
autentica
