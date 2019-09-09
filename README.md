# Ransomware-Veto-Samba

Função: 
Cria um arquivo com o parametro "veto files = " todos os arquivos conhecidos de ransomware, fazendo com que esses arquivos não sejam gravados.

Desenvolvido na versão
python >= 3.5

Crie um include no [Global]
Ex: smb.conf

[global]
        ...
        
        include = /etc/samba/ransomwares.conf

        client min protocol = SMB2
        client max protocol = SMB3
        min protocol = SMB2
        max protocol = SMB3

1 - Adicionar crontab:
# Ex: Atualização a cada 6 hora
* */6 * * * <PATH>/ransomware-smb.py

2 - Escolha da variavel "dirsamba"

ex:
dirsamba='/etc/samba'

3 - Descomentar comando Reload do Samba.

# Reload Samba
#os.system("smbcontrol smbd reload-config")
#os.system("smbcontrol nmbd reload-config")






