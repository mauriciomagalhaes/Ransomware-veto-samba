# Ransomware-veto-samba
> Cria um arquivo com o parametro "veto files = " todos os arquivos conhecidos de ransomware, fazendo com que esses arquivos não sejam gravados.

## Desenvolvido

python >= 3.5

## Installation

#Linux:

git clone https://github.com/mauriciomagalhaes/ransomware-samba.git

pip install python-dateutil

#Samba:

Crie um include no [Global]

        include = /etc/samba/ransomwares.conf

        client min protocol = SMB2
        client max protocol = SMB3
        min protocol = SMB2
        max protocol = SMB3


## Historico de Desenvolvimento

* 0.1
    * Primeira Versão

