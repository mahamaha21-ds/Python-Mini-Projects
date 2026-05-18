def addfun():
    name=input("Enter the name:",)
    mark=int(input("Enter the mark:",)) 
    file=open("stud.txt","a",newline="\n")
    file.write(name)
    file.write(str(mark))
    file.close()
    print("successfully, student detail added")

def viewfun():
    file=open("stud.txt","r")
    print(file.read())
    file.close()

def search():
    file=open("stud.txt","r")
    f=file.read()
    findname=input("enter the name of the student:",)
    if findname in f:
        print("found")
    else:
        print("Its not existed")
    file.close()

while True:
    print("Enter 1, for adding student detail:")
    print("Enter 2, for view all student details:")
    print("Enter 3, for search particular student detail")
    print("enter 4, for exit")
    details=int(input("enter 1 or 2 or 3:",))
    if details==1:
        addfun()
    elif details==2:
        viewfun()
    elif details==3:
        search()
    elif details ==4:
        print("EXIT")
        break
    else:
        print("Invalid choice")
