import os
logout = input("Do you wish to shutdown your computer? (yes/no): ")

# if shutdown == 'no':
#     exit()
# else:
#     os.system("shutdown /s /t 1")
if logout == "yes":
    os.system("shutdown -l")
else:
    exit()