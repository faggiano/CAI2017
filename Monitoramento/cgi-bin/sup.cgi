#!/bin/bash
read X
DIRET="/usr/lib/cgi-bin"
MAIL_LOG="/var/log/hardtest/sendemail"
urldecode(){
  echo -e $(sed 's/%/\\x/g')
}
touch "$DIRET/mail.txt"
#mkdir "$DIRET/log"
#touch "$DIRET/log/sendemail.log"
echo "Content-type: text/html"
echo
echo "<h1>$X</h1>"
email=$(echo $X | cut -d"&" -f1 | cut -d"=" -f2)
email=$(echo $email | urldecode )
msg=$(echo $X | cut -d"&" -f2 | cut -d"=" -f2)
msg=$(echo $msg | urldecode | tr + ' ')
echo "Email do usuário: $email" > mail.txt 2>> email.log
echo "Mensagem do usuário: $msg" >> mail.txt 2>> email.log
echo "<h5>$email</h5>"
echo "<h5>$msg</h5>"
cat <<EOFFF | sendemail -l $MAIL_LOG/sendemail.log \
-f "contato.hardtest@gmail.com" \
-u "[Contato] Comentário" \
-t "arielpaixao10@gmail.com" \
-cc "$email" \
-s "smtp.gmail.com:587" \
-o tls=yes \
-xu "contato.hardtest@gmail.com" \
-xp "hardtest@132" >> $MAIL_LOG/email.log
echo "$msg"
EOFFF                                                    
