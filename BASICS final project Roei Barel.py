import time
print("Hello, This is my Basic final project")
username = input("What is your name? ")
print("Hi " + username + ", nice to meet you")
print("This is a special calculator, I would need two numbers fro you")
flag = 0 #(flag=1, devide by zero) (flag=2, invalid operator)
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
if num1%2 == 0:
    num1_status = "even"
else:
    num1_status = "odd"
if num2%2 == 0:
    num2_status = "even"
else:
    num2_status = "odd"
print("Thank you for putting in your numbers, " + str(num1) + " and " + str(num2))
print("I can see that the first number is " + num1_status)
print("And the second is " + num2_status)
if num1_status == num2_status:
    print("So both of them are " + num1_status)
else:
    print("So one of them is " + num1_status + " and one is " + num2_status)
operator = input("Select operator(+, -, *, /): ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    sel_int = input("You chose, division, should the result be integer? (y/n) ")
    if num2 != 0:
        if sel_int == "y":
            result = num1 // num2
        else:
            result = num1 / num2
    else:
        flag = 1
else:
    flag = 2
if flag > 0:
    if flag == 1:
        print("Error: num_2 is zero")
    else:
        print("Error: Operator " + operator + " is not supported") 
    print("An error had occured, please try again")
else:
    print(str(num1) + " " + operator + " " + str(num2) + " = " + str(result))
print("Thank you " + username + " for using the calculator on " + time.ctime())






