# Prerequisite to run pyhton script
* Create Azure blob account https://azure.microsoft.com/
* Create Storage account 
* Download and instal python https://www.python.org/downloads/

# Steps to create project to run script
* Open cmd, PowerShell, or Bash and create new directory for project using command
  ```mkdir blob-test```
* Then switch to newly created project directory 
  ```cd blob-test```
* Install the required packages
  ```pip install azure-storage-blob```
* From the project directory open text file in code editor
* Use the python code from the given blob-test.py file in your new text file created in code editor
* Save the text file with any-name.py

# Steps to get azure connetion string
* Login to the Azure portal
* Locate your storage account
* In the Settings section of the storage account overview, select Access keys. Here, you can view your account access keys and the complete connection string for each key
* Copy connection string under key1 and add connection string value to an environment variable
* To add environment variable run below command
* On windows
  ```setx AZURE_STORAGE_CONNECTION_STRING "<yourconnectionstring>"```
* On Linux 
  ```export AZURE_STORAGE_CONNECTION_STRING="<yourconnectionstring>"```
* On macOS
  ```export AZURE_STORAGE_CONNECTION_STRING="<yourconnectionstring>"```
* Once environment variable added restart the program if its running to read the environment variable

# Run script
* To run the script execute below command from project directory
  ```python blob-quickstart-v12.py```
* For more information visit - https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
