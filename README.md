# Ransomware-Samba

Função: 
Cria um arquivo "veto files = " com todos os arquivos conhecidos de ransomware, fazendo com que esses arquivos não sejam gravado
crie um include no [Global]
Ex: smb.conf

[global]
        workgroup = SERVER
        realm = SERVER.LOCAL
        netbios name = CADUSMB
        server role = active directory domain controller
        server services = -dns
        dns forwarder = 192.168.1.1
        idmap_ldb:use rfc2307 = yes
        vfs objects = acl_xattr, full_audit, shadow_copy2, recycle
        map acl inherit = Yes
        store dos attributes = Yes
        include = /etc/samba/ransomwares.conf

        client min protocol = SMB2
        client max protocol = SMB3
        min protocol = SMB2
        max protocol = SMB3


Desenvolvido na versão
python >= 3.5

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






