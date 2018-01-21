#!/bin/bash
apt-get remove apache2 --purge -y
apt-get purge apache2 -y
apt-get autoremove -y
rm -rf /var/www/html/*
rm -rf /usr/lib/cgi-bin/*
