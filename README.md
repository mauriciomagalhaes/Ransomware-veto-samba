# Ransomware-veto-samba
> Cria um arquivo com o parametro "veto files = " todos os arquivos conhecidos de ransomware, fazendo com que esses arquivos não sejam gravados.

# Desenvolvido

python >= 3.5 e Versão em Bash

# Instalação

## Linux:

### Versão Python

        git clone https://github.com/mauriciomagalhaes/Ransomware-veto-samba.git

        pip install python-dateutil
        
        cd <PATH>/Ransomware-veto-samba
        
        chmod +x ransomware-veto-smb.py 
        
### Versão Bash

                Debian "apt install jq"
                Centos "yum install jq -y"
                
                ou baixe o binário 
                
                wget https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 -O /usr/sbin/jq
                chmod +x /usr/sbin/jq

1 - Adicionar crontab:

Ex: Atualização a cada 6 hora

        * */6 * * * <PATH>/ransomware-veto-smb.py
        ex: * */6 * * * /opt/scripts/Ransomware-veto-samba/ransomware-veto-smb.py
        ou
        ex: * */6 * * * /opt/scripts/Ransomware-veto-samba/ransomware-veto-smb.sh
        
2 - Escolha da variavel "dirsamba"

        Python
        dirsamba='/etc/samba'
        
        Bash
        SMBCONF='/etc/samba'

3 - Descomentar comando Reload do Samba.

## Reload Samba
Descomente as útimas linhas abaixo:
        
   #Python - Escolha o tipo de reinicialização, padrão init.d
   
        # Por smbcontrol 
        # os.system("smbcontrol all reload-config")
        #
        # Port init
        os.system("/etc/init.d/samba stop")
        time.sleep(5)
        os.system("/etc/init.d/samba start")
        # Por System
        #os.system("systemctl stop samba")
        #time.sleep(5)
        #os.system("systemctl stop samba")
        
   #Bash -  Escolha o tipo de reinicialização, padrão init.d
    
        Por smbcontrol
        #$SMBCONTROL all reload-config
        
        Por Init.d
        /etc/init.d/samba stop
        sleep(5)
        /etc/init.d/samba start
        
        Por Sytem
        #systemctl stop samba
        #systemctl stop samba


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

