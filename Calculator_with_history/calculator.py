print("CALCULATOR WITH HISTORY")
print("1,Addition")
print("2,Subtraction")
print("3,Multiplication")
print("4,Division")
user=int(input("Enter 1 or 2 or 3 or 4:",))
a=int(input("Enter num 1:",))
b=int(input("Enter num 2:",))

def add():  
     return "Addition:",a+b
def sub():
    return "Subtraction:",a-b
def mult():
    return "Multiplication:",a*b
def div():
    return "Division:",a/b


try:
    if user == 1:
        result=add()
        print(result)
    elif user == 2:
        result = sub()
        print(result)
    elif user == 3:
        result=mult()
        print(result)
    elif user == 4:
        result=div()
        print(result)
except ValueError:
    print("Enter a integer value.")
except ZeroDivisionError:
    print("Division Error, 1/0.")
finally:
    print("Calculation Done!")

f=open("calculator.txt","a")
f.write("user entered:" + str(user) + "\n")
f.write("a = " + str(a) + "\n")
f.write("b = " + str(b) + "\n")
f.write("result:"+ str(result) +"\n")
f.write("____________________________"+"\n")
f.close()


