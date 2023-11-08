user_input=input("Enter the string to be indexed: ")
list_word=user_input.split()
list_word=[elements.lower() for elements in list_word]
dictionary=[] #[{'word':'hello','count':2}]
print(list_word)
for eachUserWord in list_word:
    print(eachUserWord)
    value_present = any(eachUserWord in d.values() for d in dictionary)
    if value_present:
        for word in dictionary:
            if(word['wordName']==eachUserWord):
                word['count']+=1
        print(f"The value {eachUserWord} is present as a value in at least one dictionary.")
    else:
        newWord={}
        newWord['wordName']=eachUserWord
        newWord['count']=1
        dictionary.append(newWord)
        print("not found")

        
print(dictionary)