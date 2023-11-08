import math
def noOfCans(h,w):
    return math.ceil(h*w/7)

print(noOfCans(7,7))
def primeNumber(checker):
    count=0
    for i in range(2,checker):
        if(checker%i==0):
            count=count+1
            print(f"{checker}%{i} {checker%i}")
            print(count)
        if(count>0):
            print("Not a prime")
            break
    if(count==0):
        print("prime")


primeNumber(7)