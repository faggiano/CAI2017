#!/bin/bash

linha=$(grep ^$1\; 'login.txt')
eemail=$(echo $linha | cut -d";" -f2)
eemail=$(echo $eemail | sed s/%40/@/g)
var=$(echo $RANDOM | md5sum | cut -b1-8)
var2=$(echo $linha | cut -d";" -f3)
cat "login.txt" > "arquivo2.pwd"
var3=$(echo $var | sha256sum | cut -d" " -f1)
echo $linha | sed s/$var2/$var3/g >> 'arquivo2.pwd'
sed /$linha/d 'arquivo2.pwd' > 'login.txt'
cat <<EOFFF | sendemail -l /var/log/pingaralho/sendemail.log \
-f "senaimonitoramento@gmail.com" \
-u "[Pingaralho] Troca de senha" \
-t "$eemail" \
-cc "arielpaixao10@gmail.com" \
-s "smtp.gmail.com:587" \
-o tls=yes \
-xu "senaimonitoramento@gmail.com" \
-xp "sen@i132" >> /var/log/pingaralho/email.log
Olá $1
Você requisitou um senha nova.
Caso não tenha requisitado, entre em contato com administrador@sistema.com.br
Sua nova senha é: $var
Recomendamos que você troque sua senha na primeira oportunidade
EOFFF
