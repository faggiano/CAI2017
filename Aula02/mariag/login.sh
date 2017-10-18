#!/bin/bash 
incorreto(){
	sleep 3
	echo 
	echo "Login incorrect"	
}
while :
do
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
	[[ $LOGIN == "vagrant" ]] && [[ $PASS == "vagrant" ]] && \
	break 2 || incorreto
	count=$(($count+1))
	[[ $count == "5" ]] && \
	break
    done
done
