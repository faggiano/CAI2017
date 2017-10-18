#!/bin/bash
clear
echo "apt-get update && apt-get install apache2 -y"
apt-get update && apt-get install apache2 -y
cp /etc/apache2/conf-enabled/charset.conf /etc/apache2/conf-enabled/charset.conf.old
grep -i utf-8 /etc/apache2/conf-enabled/charset.conf.old | cut -d"#" -f2 > /etc/apache2/conf-enabled/charset.conf
a2enmod cgid
systemctl restart apache2
[[ $? == "0" ]] && echo Funcionou || echo Falhou
