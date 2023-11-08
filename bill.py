import random
user_input = input("Please enter your name in comma seperated manner: ")
values_list = user_input.split(',')
num = random.randint(0,5)

print(values_list[num],"will pay the bill")
# print(num)
# print(values_list)
# print(user_input)
