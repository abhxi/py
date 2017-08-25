from tinydb import TinyDB, Query
import getpass
def initial():
    print "Welcome to The Club"
    accountyn = raw_input("Do you have an account? Y/N")
    accountyn = accountyn.lower()
    if accountyn == "y":
        login()
    elif accountyn == "n":
        signup()
    else:
        initial()

def signup():
    
    print "Start by choosing a username."
    newusername = raw_input("Username:")
    print "Now choose a password."
    newpassword = getpass.getpass("Password:")
    userinfo = TinyDB("userinfo.json")
    userinfo.insert({newusername: newpassword})
    print userinfo.all()

