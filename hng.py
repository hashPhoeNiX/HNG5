import hashlib

usrid = [112, 221, 451, 321]
pwd = ["pass123", "my", "four", "dimitri"]
def main():
    ques = str(input("Are you a new user? y/n "))
    if ques == 'y':
        reg()
    elif ques == 'n':
        login_var()
    else:
        print("Invalid input. Input 'y' for yes or 'n' for no.")
        main()
def login_var():
    login = int(input("User ID: "))
    pswd = str(input("Password: "))
    f = hashlib.sha1(pswd.encode())
    g = f.digest()
    for i in range(len(usrid)):
        if login == usrid[i]:
            usrid[i] = pwd[i]
            a = hashlib.sha1(pwd[i].encode())
            c = a.digest()
            if c == g:
                print("Matched!")
                break
            else:
                print("Unmatched")
            break
def reg():
    try:
        newID = int(input("ID: "))
        for i in range(len(usrid)):
            if newID != usrid[i]:
                new_pwd = str(input("Password: "))
                usrid.append(newID)
                pwd.append(new_pwd)
                print("Regristration successful")
                break
            else:
                print("User " + str(newID) + " already exists.")
                main()
                break
    except ValueError:
        print("Hint: User ID is an integer.")
        main()
main()
