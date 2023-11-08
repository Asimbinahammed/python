initialDict={
    'aswin':90,
    'asim':100,
    'anju':88,
    'visu':56,
    'paru':42
}

for index, key in enumerate(initialDict):
    print(f"Index: {index}, Key: {key}, Value: {initialDict[key]}")
print(len(initialDict))

def markChecker(marks):
    if(marks>=90):
        return "A+"
    elif(marks>=80):
        return "A"
    elif(marks>=50):
        return 'B'
    else:
        return 'F'

for name in initialDict:
    marks=initialDict[name]
    print(marks)
    grade=markChecker(marks)
    # print(grade)
    initialDict[name]=grade
print(initialDict)
def adding_new(name,grade):
    initialDict[name]=grade
    return initialDict

print(adding_new('remani','B'))