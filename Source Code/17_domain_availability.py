# Python program to check domain avaliability
import whois
import socket

# function to test internet connection
def test_connection():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return

# driver code
if __name__ == "__main__":
    test = test_connection()
    if test == True:
        check = input("Enter the domain name to check: ")
        domain = whois.whois(check)
        if domain.domain_name == None:
            print("this domain is available")
        else:
            print("Sorry! This domain already purchased")
    else:
        print("You are not connected to internet")
