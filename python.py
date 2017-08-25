import tinydb
import getpass
def initial():
    print "Welcome to The Club"
    accountyn = raw_input("Do you have an account? Y/N")
    accountyn = accountyn.lower()
    if accountyn = y:
        login()
    else:
        signup()

def signup():
    
    print "Start by choosing a username."
    newusername = raw_input("Username:")
    print "Now choose a password."
    new_password = getpass.getpass("Password:")
    
