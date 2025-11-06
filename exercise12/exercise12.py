import random
number = random.randint(1,100)
print(number)


user=0
i=0
while number!=int(user):

    user= input('please enter number between 1 and 100 ')
    try:
        user_num =int(user)
    except:
        print('input should be number') 
        quit()   
    if number > int(user_num):
            print ('Random number is bigger')
    elif number < int(user_num):
            print('random number is less')
    i+=1
    print ("you won the game in  "+str(i)+" attempts")
