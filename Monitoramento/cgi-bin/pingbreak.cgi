#!/bin/bash
clear
launch(){ source pingd.cgi & ; }
cease(){ killall menu.cgi ; }
case $1 in
	"start") launch ;;
	"stop") cease ;;
	*) ;;
esac
