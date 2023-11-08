# def number_to_alphabet_equivalent(number):
#     alphabet_offset = ord('A')  # ASCII code of 'A'
#     print(alphabet_offset)
#     number_str = str(number)
#     equivalent_alphabet = ''.join(chr(int(digit) + alphabet_offset) for digit in number_str)
#     return equivalent_alphabet

# # Example usage
# number = 12345
# equivalent_alphabet = number_to_alphabet_equivalent(number)
# print(equivalent_alphabet)  # Output: BCDEF
# ciperedText=""
# result_list=[]
# c=0
# def cipering(shiftValue, text):
#     for i in range(len(text)):
#         for j in range (26):
#             indexFound=alphabets.index(text[i])
#             result_list.append(alphabets[indexFound+shiftValue])
#         print(c)
#         result_list.append(text[i])
#     result = ''.join(result_list)
#     print(result)
result=''
result_list = []
def cipering(shiftValue, text):
     for i in range(len(text)):
          if text[i].isalpha():
            index=alphabets.index(text[i])
            result=alphabets[(index+shiftValue)%26]
            result_list.append(result)
          else:
              result_list.append(text[i])
        #   print(result_list)
     result = ''.join(result_list)
     return result
alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
userSelection=input("Enter Encrypt or Decrypt: ")
shiftValue=int(input("Enter the shift value: "))
text=input("Enter the message: ")
if(userSelection.lower()=="e"):
    endResult=cipering(shiftValue,text)
    print(endResult)
    print("encrypt")
elif(userSelection.lower()=="decrypt"):
     print("decrypt")
else:
     print("invalid entry")
