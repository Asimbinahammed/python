import random

print('Welcome to hangman game')
guessedList = ["potato","apple","orange","ladyfinger"]
chosenWord = random.choice(guessedList)
dashedFormat=[]
print(chosenWord)
a=[]
length = len(chosenWord)
print("length ", length)
for i in range(length):
    new="-"
    dashedFormat+=new
    a.append(chosenWord[i])
#     print(dashedFormat)
print("dashedFormat outside function",dashedFormat)
print("a outside function",a)
originalChosenOne=a
hangfigure="__\n| |\n  |"
i=0
print(hangfigure)

def switch_case(i):
            if i == 1:
                print("__\n| |\n0 |")
            elif i == 2:
                print("__\n| |\n0 |\n|")
            elif i == 3:
                print("__\n| |\n0 |\n/|")
            elif i == 4:
                print("wrong")
                # print("__\n| |\n0 |\n/|\")
            elif i == 5:
                print("__\n| |\n0 |\n/|\\n|")
            else:
                print("Invalid option")
while i<6:
    userInput = input(f"You have {i} chances left. \n enter a letter to guess: ")    
    indices = [index for index, entry in enumerate(a) if entry == userInput]
    print(indices)
    count=a.count(userInput)
    print("count ",count)
    if(len(indices)>0):
        #postive cases
        print("u guessed right!!!")
        for j in range (len(indices)):
            dashedFormat[indices[j]]=a[indices[j]]
        print("dashedFormat after finding a match",dashedFormat)
        checkForFull = [index for index, entry in enumerate(dashedFormat) if entry == "-"]
        if(len(checkForFull)==0):
            print("u win!!!")
            break
    else:
        i+=1
        print(f"i : {i}")
        switch_case(i)
        
















    #  if count>0:
    #     for i in range():
    #         pos = a.index(userInput)
    #         dashedFormat[pos]=userInput
    #         a.remove(userInput)
    #         print("position ",pos)
    #         print("a inside fucntion",a) 
    #     print("You have guessed right",dashedFormat)
    # else:
    #     #not found cases
        #print("you have guessed wrong")   

