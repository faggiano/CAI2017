#!/bin/bash
pinging(){
clear
echo "" > ../report/reports
IPAS=$(cat iprange.txt)
arp -a > macip.txt
for desc in $(cat ../../equipments/db/equipments.csv | cut -d";" -f1) ; do
        for mac in $(grep ^$desc\; ../../equipments/db/equipments.csv | cut -d";" -f4) ; do
		ip=$(grep $mac macip.txt | cut -d" " -f2 | cut -d"\(" -f2 | cut -d"\)" -f1)
                ping -W 1 -c 1 -i 1 $ip & > /dev/null
                user=$(grep ^$desc\; ../../equipments/db/equipments.csv | cut -d";" -f3)
                if [[ $? == "0" ]] ; then
                        echo \[$(date)\]: $mac' ->' $desc': UP' >> reportd 
                        echo "$desc;UP" >> reports

                else
                        echo \[$(date)\]: $mac' ->' $desc': UP' >> reportd
                        echo "$desc;DOWN" >> reports
                fi
        done
done ; }
pinging
