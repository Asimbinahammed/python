row1=['😎','😎','😎']
row2=['😎','😎','😎']
row3=['😎','😎','😎']
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
userSelect=input("Pls select your position: ")
rowNumber=int(userSelect[0])
columnNumber=int(userSelect[1])
rowUserSelected=matrix[rowNumber-1]
rowUserSelected[columnNumber-1]='X'
print(f"{row1}\n{row2}\n{row3}\n")

print()
# print(userSelect)
# print(rowNumber)