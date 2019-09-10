#!/bin/bash

# instale o comando jq 

SMBCONF="/etc/samba"
SMBCONTROL=$(which smbcontrol)
JQ=$(which jq)
TOTALREG=$(jq -r .api.file_group_count $SMBCONF/ransomwares.json)
DATA=$(jq -r .lastUpdated $SMBCONF/ransomwares.json)

while true; do
    if curl --output /dev/null --silent --head --fail https://fsrm.experiant.ca/api/v1/combined; then
        curl -o /etc/samba/ransomwares.json https://fsrm.experiant.ca/api/v1/combined && break
    fi
done

echo "Total de Ransomwares conhecidos: $TOTALREG"
echo "Ultima Atualização: $DATA"

$JQ -r .filters[] $SMBCONF/ransomwares.json > $SMBCONF/ransomwares.conf

sed -i 's/^/\//g' $SMBCONF/ransomwares.conf
sed -i ':a;N;s/\n//g;ta' $SMBCONF/ransomwares.conf
sed -i 's/^/veto files = /g' $SMBCONF/ransomwares.conf

/etc/init.d/samba stop
sleep 5
/etc/init.d/samba start
#$SMBCONTROL smbd reload-config
#$SMBCONTROL/smbcontrol nmbd reload-config
