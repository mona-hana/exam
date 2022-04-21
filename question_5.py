# question 5
from random import randint

rnd = randint(0, 10)
print("random number : " , rnd)

x = int(input("choice your first guess between (0 ,10 ): "))
if (x<10 and x>0):

    if x==rnd :
        print("you are winer")
    
    else :
            y= int(input("wrong ,choice your second guess between (0 ,10 ) : "))

            if (y<10 and y>0):
                if rnd == y:
                    print("you are winer")

                    
                else:
                    z =int(input("wrong ,choice your third guess between (0 ,10 ) : ")) 
                    
                    if (z<10 and z>0):
                        if rnd == z:
                            print("you are winer")
                        
                        else:

                            print(" sorry \n your choice over \n try again later") 
                    else:

                            print("error , this number is incorrect")

                            
            else:print("error , this number is incorrect")

else:
    print("error , this number is incorrect")