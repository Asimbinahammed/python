my_list = ["apple", "banana", "cherry", "apple", "date", "apple"]
search_entry = "apple"

indices = [index for index, entry in enumerate(my_list) if entry == search_entry]
print(f"The entry '{search_entry}' is found at indices: {indices}")

for i in range(len(indices)):
    print(indices[i])