#!/bin/bash
PASSWD="/home/vagrante/CAI/kamilas/passwd"
incorreto(){ dialog --msgbox "Login incorrect" 0 0; autenticacao ; }
autenticacao(){ 
while : ; do
	LOGIN=$(dialog --stdout --title "Login: " \
 --inputbox "Digite o seu usuário: " 0 0 )
	PASSW=$(dialog --stdout --title "Password"\
--passwordbox "Digite sua senha" 0 0) 
[[ -Z $LOGIN ]] && incorreto
[[ -Z $PASSW ]] && incorreto
PASSW=$(echo $PASSW | sha256sum | cut -d" " -f1)
if [[ $(grep $LOGIN $PASSWD) ]]
then
 	SENHA=$(grep $LOGIN $PASSWD | cut -d";" -f2)
 	[[ $PASSW == $SENHA ]] && break 3 || incorreto
 else
     incorreto
fi
   done # Segunda Loop
}
autenticacao
