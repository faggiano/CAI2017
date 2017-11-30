#!/bin/bash
read X
urldecode(){
  echo -e $(sed 's/%/\\x/g')
}
chmod 777 sendemail.log
chmod 777 email.log
chown www-data:www-data sendemail.log
chown www-data:www-data email.log
echo "Content-type: text/html"
echo
email=$(echo $X | cut -d"&" -f1 | cut -d"=" -f2)
email=$(echo $email | urldecode )
msg=$(echo $X | cut -d"&" -f2 | cut -d"=" -f2)
msg=$(echo $msg | urldecode | tr + ' ')
email=$(echo "Email do usuário: $email")
msg=$(echo "Mensagem do usuário: $msg")
echo "<script>alert('Mensagem enviada. Aperte [OK] para voltar.')</script>"
echo "<meta http-equiv="refresh" content=0;url="../index.html">"
sendemail -l sendemail.log                         \
-f "senaimonitoramento@gmail.com"                              \
-u "[Contato] Comentário"                                    \
-t "pedroreiki030802@gmail.com"                                 \
-m "$email\n$msg"                                            \
-cc "$email"                                                 \
-s "smtp.gmail.com:587"                                      \
-o tls=yes                                                   \
-xu "senaimonitoramento@gmail.com"                             \
-xp "sen@i132" >> email.log
