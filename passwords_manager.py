from cryptography.fernet import Fernet 




# we call these function only one time 
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file :
        key_file.write(key)

write_key()
    
    
def load_key():
    file= open ("key.key","rb")
    key = file.read()
    file.close()
    return key

master_password = input(" What is the master password :")

key = load_key() #+ master_password.encode()
fer =Fernet(key)

def view():
    with open('passwords.txt','r') as f : 
        for line in f.readlines():
            data = line.rstrip()
            user , pwd = data.split("|")
            print("user:",user,", password:",fer.decrypt(pwd.encode()).decode())



def add():
    name = input("Account name :")
    psswd = input(" Password :")
    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(psswd.encode()).decode() + "\n")
 

while True : 
    option = input("Do you want to add a new password to your list or view the list ,(view/add)  . press q to quit: ")
    if option == "q":
        break
    if option == "view":
        view()
    elif option == "add":
        add()
    else : 
        print("Not in options .")
        continue 
       