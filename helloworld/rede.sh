
#!/bin/bash
clear
echo "Digite o nome da interface"
read INTERFACE
echo "Digite o nome do endereco IP"
read ENDERECO
$(ip link set dev $INTERFACE down)
$(ip address flush dev $INTERFACE)
$(ip address add $ENDERECO dev $INTERFACE)
$(ip link set dev $INTERFACE up)
clear
echo "Hello World! Script de rede executado!"
