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
   
    print(  " %-20s %-20s" % (n, info[n]))
