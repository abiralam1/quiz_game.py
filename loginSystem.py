from tkinter import*


def newaccount():
    db = open("database.txt","r")
    Username = input("Create username:")
    Password = input("Create password:")
    Password1 = input("Confirm password:")
    d=[]
    f=[]
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data =dict(zip(d, f))

    if Password != Password1:
        print("Passwords don't match, restart")
        newaccount()
    else:
        if len(Password)<=6:
            print("Password too short,restart")
            newaccount()
        elif Username in d:
            print("username exists")
            newaccount()
        else:
            db = open("database.txt", "a")
            db.write(Username+","+Password+"\n")
            print("Success")

def login():
    db = open("database.txt", "r")
    Username = input("Enter your username:")
    Password = input("Enter your password")

    if not len(Username or Password)<1:
        d=[]
        f=[]
        for i in db:
            a,b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data =dict(zip(d, f))

        try:
            if data[Username]:
                try:
                    if Password ==data[Username]:
                        print("Login success")
                        print("Hi,",Username)
                    else:
                        print("Password or Username incorrect")
                except:
                    print("Incorrect password or username")
            else:
                print("Username or password doesn't exist")
        except:
            print("Username or password doesn't exist")
    else:
        print("Please enter a value")
def home(option=None):
    option = input("Login | Signup:")
    if option =="Login":
        login()
    elif option=="Signup":
        newaccount()
    else:
        print("Please enter an option")
    home()
window = Tk()

titleLabel= Label(window,text="Enter your Login",font=("Arial",25)).grid(row=0,column=0,columnspan=2)


usernameLabel = Label(window,text="Username: ",width=20).grid(row=1,column=0)
usernameEntry = Entry(window).grid(row=1,column=1)

passwordLabel = Label(window,text="Password: ",width=20).grid(row=2,column=0)
passwordEntry = Entry(window).grid(row=2,column=1)

button = Button(window, text="Login", command=login)
button.grid(columnspan=2)

button = Button(window,text="New Account",
                          command=newaccount)
button.grid()



window.mainloop()