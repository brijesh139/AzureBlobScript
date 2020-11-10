#!/bin/bash
export AZURE_STORAGE_ACCOUNT="storagenameblobone"
export AZURE_STORAGE_ACCESS_KEY="t5Z5LN1zaAlr27gW+3q6rgCkiWNKm7oXYHYr/T4gkka25NLNgj/o7th0pzAqVZwzjrRlLyhlBETGMssd3B9yyQ=="
export AZUR_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=storagenameblobone;AccountKey=t5Z5LN1zaAlr27gW+3q6rgCkiWNKm7oXYHYr/T4gkka25NLNgj/o7th0pzAqVZwzjrRlLyhlBETGMssd3B9yyQ==;EndpointSuffix=core.windows.net"
#login
# az login

# Create a resource group
az group create \
--name myResourceGroup \
--location eastus

# Create a container
az storage container create \
--name mycontainer

# Create sample files to upload as blobs
for i in `seq 1 3`; do
    echo $RANDOM > container_size_sample_file_$i.csv
done

# Upload sample files to container
az storage blob upload-batch \
--account-name $AZURE_STORAGE_ACCOUNT \
  --account-key $AZURE_STORAGE_ACCESS_KEY \
    --pattern "container_size_sample_file_*.csv" \
    --source . \
    --destination mycontainer


# Download file
sudo az storage blob download-batch \
 --account-name $AZURE_STORAGE_ACCOUNT \
  --account-key $AZURE_STORAGE_ACCESS_KEY \
  -d ./download \
  -s mycontainer \
  --pattern container_size_sample_file_1.csv
\

