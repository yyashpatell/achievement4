def add(num1,num2):
        print(num1+num2)
        return
def sub(num1,num2):
        print(num1-num2)
        return
def mul(num1,num2):
        print(num1*num2)
        return
def div(num1,num2):
        print(num1/num2)
        return
def modulusDivision(num1,num2):
        print(num1%num2)
        return
    
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. modulusDivision")

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

choice=int(input("enter your choice (1,2,3,4,5):"))
if choice==1:
    add(num1,num2)
elif choice==2:
    sub(num1,num2)
elif choice==3:
    mul(num1,num2)
elif choice==4:
    div(num1,num2)
elif choice==5:
    modulusDivision(num1,num2)
else:
    print("wrong choice!!!")

    