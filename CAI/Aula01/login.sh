#!/bin/bash
usuario="Thales"
senha="0ed5a4f0a1bed1b93113d77361b90b202cf85985e4f9d59ba4ff404a0100dc11"
criar(){
	CRIAUSU=$(dialog --stdout						\
				--title "Criar Usuario"				\
				--inputbox 							\
					"Qual o nome do usuario que deseja criar?" \
				0 0)
	useradd -m -s /usr/bin/tcsh $CRIAUSU
	[[ $? == 0 ]] && $(passwd $CRIAUSU ; CONT=$?) || CONT=$?
	CONT=($CONT + $?)
	if [[ $CONT == 0 ]]; then
		dialog --msgbox "Usuario criado com sucesso..." 0 0
	else
		dialog --msgbox "Ocorreu falha na criação do usuário" 0 0
	fi
	menu
}
remover(){
	REMOVER=$(dialog --stdout 						\
				--title "Remover Usuário"			\
				--inputbox							\
					"Qual o nome do usuario que deseja remover?" \
				0 0) 
	userdel -rf $REMOVER
	CONT=$?
	if [[ $CONT == 0 ]]; then
		dialog --msgbox "Usuario removido com sucesso..." 0 0
	else
		dialog --msgbox "Ocorreu falha na remoção do usuário" 0 0
	fi
	menu
}
visualizar(){
	dialog --title "Usuários" --textbox /etc/passwd 0 0	
}
opcao(){
	case $1 in
		1) criar ; menu ;;
		2) remover ; menu ;;
		3) visualizar ; menu ;;
		4) clear ; exit 0 ;;
		*) dialog --msgbox "Opção inválida." 0 0 ; menu ;;
	esac
}
menu(){
	OPCOES=$(dialog --stdout						\
			--title "MENU"							\
			--menu "Digite uma das opções: "		\
			0 0 0 									\
			1		"Criar usuário"					\
			2		"Remover usuário"				\
			3		"Visualizar usuários"			\
			4		"Sair")	
	opcao $OPCOES
}
logar(){
	USER=$( dialog 									\
			--stdout 								\
			--title "Usuário"						\
			--inputbox "Digite o nome do usuário: " \
			0 0)
	PASS=$( dialog									\
			--stdout								\
			--title "Senha"							\
			--passwordbox "Digite sua senha: " 		\
			0 0)
	PASS=$(echo $PASS | sha256sum | cut -d" " -f1)
	[[ $USER == $usuario ]] && [[ $PASS == $senha ]] && menu || logar
}
logar
