import os
restart = input("Do you wish to shutdown your computer? (yes/no): ")

# if shutdown == 'no':
#     exit()
# else:
#     os.system("shutdown /s /t 1")
if restart == "yes":
    os.system("shutdown /r /t 1")
else:
    exit()