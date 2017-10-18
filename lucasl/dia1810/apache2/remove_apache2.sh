#!/bin/bash
clear
apt-get remove apache2 --purge
apt-get purge apache2
apt-get autoremove
rm -rf /etc/apache2
rm -rf /var/www/html/*
rm -rf /usr/lib/cgi-bin/*
