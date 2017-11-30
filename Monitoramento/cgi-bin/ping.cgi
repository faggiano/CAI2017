#!/bin/bash
echo "content-type: text/html"
echo
echo "<html>"
pinging(){
echo "<body>"
clear
echo "" > .reports
for name in $(cat equipments.csv | cut -d";" -f1) ; do
        for ip in $(grep ^$name\; .equipments.csv | cut -d";" -f2) ; do
                ping -W 1 -c 1 -i 1 $ip & > /dev/null
                user=$(grep ^$name\; .equipments.csv | cut -d";" -f3)
                if [[ $? == "0" ]] ; then
		echo "<meta http-equiv="refresh" content=1;"URL=../menum.html">"
                        echo \[$(date)\]: $ip' ->' $name': UP' >> .reportd 
                        echo "$name;$user;UP" >> .reports

                else
                        echo \[$(date)\]: $ip' ->' $name': UP' >> .reportd
                        echo "$name;$user;DOWN" >> .reports
                fi
        done
done
echo "</body>" 
}
pinging
echo "</html>"
