import random
randomNumber = random.randint(1,10)
print (randomNumber)
attempt=0
while (True):
    attempt+=1
    guessedNum = int ( input ("Please enter your guessed Number: " )   )
    if (guessedNum > randomNumber):
        print("you have entered a larger number")
    elif (guessedNum < randomNumber ):
        print("you have entered a smaller number")
    elif ( guessedNum == randomNumber):
        print("Congrats you have entered the correct number")
        print("Total attempts: ", attempt)
        break


