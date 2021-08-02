def main():
    #write your code below this line
    name = input("Enter username:")
    password = input("Enter password:")

    if (name == "grace" and password == "hopper") or (name == "emma" and password == "haskell"):
        print("You have succefffully logged in!")
    else:
        print("Incorrect username or password!")

if __name__ == '__main__':
    main()
