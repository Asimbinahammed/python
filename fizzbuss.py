limit=int(input("Enter the limit: "))
for i in range(0,limit):
    if(i%5==0 and i%3==0):
        print("FizzBuzz ")
    elif(i%3==0):
        print("Fizz ")
    elif(i%5==0):
        print("Buzz")
    else:
        print(f"{i}")