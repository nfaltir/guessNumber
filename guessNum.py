import random
<<<<<<< HEAD
anyNum = random.randint(1,9)
#print(anyNum) <-------- test

guessEntry = 0
count =0

while guessEntry != anyNum and guessEntry != 'Quit':

    guessEntry = input("Enter a number between 1 and 9:")

    if guessEntry == 'Quit':
        break
    #sets counter
    count +=1
    
    guessEntry = int(guessEntry)

    if guessEntry >=1 and guessEntry <= 9:
        if guessEntry > anyNum:
            print("Too High")
        
        elif guessEntry < anyNum:
            print ("Too low")
=======
anyNum = random.randint(1, 9)
# print(anyNum) <-------- test
print("\n=============================High or Low Game=============================")
guessEntry = 0
count = 0
maxRange = int(input("Enter max range:"))
while guessEntry != anyNum and guessEntry != 'Quit':

    guessEntry = input("Enter a number between 1 "+"and "+str(maxRange)+":")

    if guessEntry == 'Quit':
        break
    # sets counter
    count += 1

    guessEntry = int(guessEntry)

    if guessEntry >= 1 and guessEntry <= 9:
        if guessEntry > anyNum:
            print("Too High")

        elif guessEntry < anyNum:
            print("Too low")
>>>>>>> Added image of output, fixed user input logic
        elif guessEntry == anyNum:
            print("\nBINGO YOU DID IT, the answer is:", anyNum)
            print("\nit took you", count, "tries\n")
    else:
        invalidEntry = guessEntry
        print("invalid entry, please use a number between 1-9")
<<<<<<< HEAD

    
=======
>>>>>>> Added image of output, fixed user input logic
