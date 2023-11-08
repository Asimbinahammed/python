import math
class matrixCreation:
    def create(self, s:str, numRows:int)->str:
        length=len(s)
        print(length)
        rows=[]
        matrix=[]
        numCols= math.ceil(length/numRows)
        print(numCols)
        for i in range(0,numRows):
            startingIndex=i*numCols
            print("starting index",startingIndex)
            for j in range (startingIndex,startingIndex+numCols):
                rows.append(s[j])
                print(rows)
            matrix.append(rows)
                
        print(matrix)            
                    
myinstance=matrixCreation()
result= myinstance.create("abcasdqwe",3)