import os
shutdown = input("Do you wish to shutdown your computer? (yes/no): ")

if shutdown == "yes":
    os.system("shutdown /s /t 1")
else:
    exit()