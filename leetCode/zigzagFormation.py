class Solution:
    def convert(self, s: str, numRows: int) -> str:
       length=len(s);
       for rows in range(0,numRows):
            print(rows)
            rowMatrix=[]
            for col in rows:
                print(col)
                rowMatrix.append(s)
                


my_instance = Solution()
result = my_instance.convert("pythonprogramming", 5)
