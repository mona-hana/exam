
# question 4

print("calculate")

number_1 = float(input("select first number of calculate: "))

number_2 = float(input("select second number of calculate: "))

action = input("select action betwen ( + , _ , * , / ) ")


def add(a, b):
    c = a+b
    return c


def multi(a, b):
    c = a*b
    return c


def divid(a, b):
    c = a/b
    return c


def sub(a, b):
    c= a-b
    return c


if action == '+':
    print(add(number_1, number_2))

if action == '-':
    print(sub(number_1, number_2))

if action == '*':
    print(multi(number_1, number_2))

if action == '/':
    print(divid(number_1, number_2)) 
