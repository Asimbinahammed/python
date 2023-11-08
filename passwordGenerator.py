import string
import random
numbers = []  
password=str()
def random_capital_letter():
    return random.choice(string.ascii_uppercase)

def random_numbers():
    return random.randint(0,9)

def random_smallLetter():
    return random.choice(string.ascii_lowercase)

def random_special_character():
    return random.choice(string.punctuation)

for i in range(8):
    pos=random.randint(1,4)
    numbers.append(pos)
    if(pos==1):
        newpass=random_capital_letter()
    elif(pos==2):
        newpass=random_smallLetter()
    elif(pos==3):
        newpass=random_special_character()
    else:
        newpass=str(random_numbers())
    
    password=password+newpass
    print(password)
    print(numbers)
    # print(pos)
# print(random_special_character())
if 1 not in numbers:
    newpass=random_capital_letter()
    password=password+newpass
if 2 not in numbers:
    newpass=random_smallLetter()
    password=password+newpass
if 3 not in numbers:
    newpass=random_special_character()
    password=password+newpass
if 4 not in numbers:
    newpass=random_numbers()
    password=password+newpass

print(password)
