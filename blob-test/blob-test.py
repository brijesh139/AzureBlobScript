import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:

    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = "blobtestnew" + str(uuid.uuid4())

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    # Create a file in local data directory to upload and download
    local_path = "./"
    local_file_name = "filenew" + str(uuid.uuid4()) + ".csv"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    file = open(upload_file_path, 'w')
    file.write("test, blob, upload, new")
    file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

        print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

    # Download the blob to a local file
    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.csv', 'DOWNLOAD.csv'))
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    # Clean up
    print("\nPress the Enter key to begin clean up")
    input()

    print("Deleting blob container...")
    container_client.delete_container()

    print("Deleting the local source and downloaded files...")
    os.remove(upload_file_path)
    os.remove(download_file_path)
# E:\blob-quickstart-v12\data\quickstartc4ddfe41-4d4a-4d42-80f5-df323a408bc0.csv
    print("Done")

except Exception as ex:
    print('Exception:')
    print(ex)