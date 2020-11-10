# Prerequisite to run pyhton script
* Create Azure blob account https://azure.microsoft.com/
* Create Storage account
* Windows Subsystem for Linux
  ## Steps to enable Windows Subsystem for Linux (WSL)
  * In windows search type "Turn windows feature on or off" and select
  * Look for Windows Subsystem for Linux and Virtual machine paltform and select check box
  * Or You can just run this command from PowerShell as admin to enable WSL ```dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart```
  * Restart system
* Install and setup Ubuntu from microsoft store (Might ask for restart)
* Open Ubuntu and run command ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash``` to install packages

# Steps to run script
* Copy given Azureblob.sh file to your local machine
* Replace AZURE_STORAGE_ACCOUNT, AZURE_STORAGE_ACCESS_KEY, AZUR_STORAGE_CONNECTION_STRING with your account details
* First run ```az login``` from ubuntu to login to the azure account 
* Run bash script using command ```~/Azureblob.sh```

## Note 
* This is the working directory of ubuntu on windows ```C:\Users\<pc-name>\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_hwer3453dfew\LocalState\rootfs\home\pc-name``` 
* Copy given bash file to this location to run or navigate to directory where bash file is copied
