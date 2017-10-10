#!/bin/bash

PASSWD="/home/vagrant/CAI/CAI/brendar/passwd"
incorreto(){ dialog --msgbox "Login incorrect" 0 0; }

while : ; do
 LOGIN=$(dialog --stdout --title "Login" \
 --inputbox "Digite seu usuário " 0 0)
 PASSW=$(dialog --stdout --title "Password" \
 --passwordbox "Digite a sua senha" 0 0)
 PASSW=$(echo $PASSW | sha256sum | cut -d" " -f1)
 
 [[ $LOGIN == "" ]] || [[ $PASSW == "" ]]
then
incorreto
else


 if [[ $(grep $LOGIN $PASSWD) ]]
 then
 	SENHA=$(grep $LOGIN $PASSWD | cut -d";" -f2)
	[[ $PASSW == $SENHA ]] && break || incorreto
 else
 	incorreto
 fi

fi
done
clear
