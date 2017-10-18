#!/bin/bash
incorreto(){ sleep 3; echo; echo "Login incorrect"; }
while : ; do #primeiro loop
	clear
	echo 
	echo "Debian GNU/Linux 8 jessie tty1"
	echo
	count=0
	while : ; do #segundo loop
		read -p "jessie login: " LOGIN
		read -s -p "Password: " PASSWD
		echo
		[[ $LOGIN == "vagrant" ]] && [[ $PASSWD == "vagrant" ]] && \
		break 2 || incorreto
		count=$(($count+1))
		[[ $count == "5" ]] && break
	done #segundo loop
done #primeiro loop
