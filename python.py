from tinydb import TinyDB, Query, where
import getpass

userinfo = TinyDB("userinfo.json")

def initial():
    print "Welcome to The Club"
    accountyn = raw_input("Do you have an account? Y/N ")
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
    if userinfo.contains(where("Username") == newusername):
        fail_user_taken()
    print "Now choose a password."
    newpassword = getpass.getpass("Password:")
    userinfo.insert({"Username": newusername, "Password": newpassword})
    print "Thanks! Now you can log in with your new account."
    login()

def login():
    print "Enter your username."
    usernametry = raw_input("Username: ")
    print "Now enter your password."
    passwordtry = getpass.getpass("Password: ")
    if userinfo.contains((where("Username") == usernametry) & (where("Password") == passwordtry)):
        success()
    else:
        fail()
    
def success():
    print "Success!"

def fail():
    print "Your username or password was incorrect."
    tryagain = raw_input("Would you like to try again? Y/N ")
    tryagain = tryagain.lower()
    if tryagain == "y":
        login()
    else:
        print "Have a nice day!"

def fail_user_taken():
    print "The username is already taken"
    tryagain = raw_input("Would you like to try again? Y/N")
    tryagain = tryagain.lower()
    if tryagain == "y":
        signup()
    else:
        print "Have a nice day!"
initial()
