from random import randint


# quesion 1


counter = int(input("please enter number of user : "))


def name():
    name = input("please enter your name :")
    return name


def family():
    family = input("please enter your family :")
    return family


info = {}
namesList = []
familiesList = []
i = 0
while i < counter:

   # namesList[i] = names()
    # familiesList[i] = families()

    namesList.insert(i, name())

    familiesList.insert(i, family())

    info[namesList[i]] = familiesList[i]
    i = i+1


for n in info:

    print(" %-20s %-20s" % (n, info[n]))


# question 2

vocab = input("please enter your vocab : ")
inverseVocab = ""
n = len(vocab)
i = n-1
while i > 0 or i == 0:
    inverseVocab = inverseVocab+vocab[i]
    i = i-1

print(inverseVocab)

# question 3



count = int(input("please enter number of list : "))
i = 0
numList = []
while i < count:
    num = int(input("your number :"))
    numList.insert(i, num)
    i += 1

for number in range(len(numList)):
    min = number

    for j in range(number, (len(numList))):
        if numList[min] > numList[j]:
            min = j

    numList[min], numList[number] = numList[number], numList[min]

print(numList)


# question 4


number_1 = int(input("select first number of calculate: "))

number_2 = int(input("select second number of calculate: "))

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


# question 5


rnd = randint(0, 10)
print("random number : " , rnd)

x = int(input("choice your first guess : "))
if x==rnd :
     print("you are winer")
   
else :
        y= int(input("wrong ,choice your second guess : "))
        if rnd == y:
            print("you are winer")

            
        else:
            z =int(input("wrong ,choice your third guess : ")) 
            
            if rnd == z:
                print("you are winer")
              
            else:

                print(" sorry \n your choice over \n try again later") 





  

   
                
