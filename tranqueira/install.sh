#!/bin/bash
falhou(){
	case $1 in
	instalacao)
		echo "O programa falhou na instalacao"
		exit 0 ;;
	*)
		echo "O programa falhou. Causa desconhecida"
		exit 0 ;;
	esac
}
apt-get update && apt-get install apache2 -y || falhou instalacao
a2enmod cgid
cp /etc/apache2/conf-enabled/charset.conf charset.conf.bkp
echo "AddDefaultCharset UTF-8" >> /etc/apache2/conf-enabled/charset.conf
$(systemctl restart apache2)
cp -R /var/www/html /var/www/html.bkp
cp -R /usr/lib/cgi-bin /usr/lib/cgi-bin.bkp
cp -R ./html /var/www
cp -R ./cgi-bin /usr/lib

