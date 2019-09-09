# Ransomware-veto-samba
> Cria um arquivo com o parametro "veto files = " todos os arquivos conhecidos de ransomware, fazendo com que esses arquivos não sejam gravados.

# Desenvolvido

python >= 3.5

# Instalação

## Linux:

        git clone https://github.com/mauriciomagalhaes/Ransomware-veto-samba.git

        pip install python-dateutil
        
        cd <PATH>/Ransomware-veto-samba
        
        chmod +x ransomware-veto-smb.py 

1 - Adicionar crontab:

Ex: Atualização a cada 6 hora

        * */6 * * * <PATH>/ransomware-veto-smb.py

2 - Escolha da variavel "dirsamba"

Ex: 

        dirsamba='/etc/samba'

3 - Descomentar comando Reload do Samba.

## Reload Samba
Descomente as útimas linhas abaixo:

        os.system("smbcontrol smbd reload-config")
        os.system("smbcontrol nmbd reload-config")


## Samba:

Crie um include em smb.conf no [Global] ou em qualquer outro compartilhamento.

        include = /etc/samba/ransomwares.conf

        #Desativando o protocolo SMB1 - WindosXp não irá funcionar
        
        client min protocol = SMB2
        client max protocol = SMB3
        min protocol = SMB2
        max protocol = SMB3


# Historico de Desenvolvimento

* 0.1
    * Primeira Versão

