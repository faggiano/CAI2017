#!/bin/bash
falhou(){
	case $1 in
	instalacao)
		echo "O programa falhou durante a instalacao"
		exit 0 ;;
	copia)
		echo "O programa falhou durante a cópia"
		exit 0 ;;
	*) 
		echo "O programa falhou. Erro desconhecido"
	esac
}
apt-get update && apt-get install dialog -y || falhou instalacao
cp -R ./dialogaralho /usr/share/dialogaralho || falhou copia
ln -s /usr/share/dialogaralho/dialogaralho /usr/bin/dialogaralho || falhou

