#!/bin/bash
read gaspar
USER=$(echo $gaspar | cut -d"&" -f1 | cut -d"=" -f2)
PASS=$(echo $gaspar | cut -d"&" -f2 | cut -d"=" -f2)
[[ $USER == "thales" ]] && [[ $PASS == "thales" ]] && \
	. menu.cgi || . falhou.cgi
