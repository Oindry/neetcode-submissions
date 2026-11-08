class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL= len(matrix), len(matrix[0])
        top, bot= 0, ROW-1
        s=""
        while  top<bot:
            row= top+(bot-top)//2
            if(target==matrix[row][-1] or target==matrix[row][0] ):
                return True
            else:
                if(target>matrix[row][-1]):
                    top= row+1
                elif(target<matrix[row][0]):
                    bot= row-1
                else:
                    s="Got"
                    break
       
        if top>bot:
            return False

        
        row= top+(bot-top)//2
        

        
        l,r=0, COL-1
        while l<r:
            mid= l+(r-l)//2
            
            if target== matrix[row][mid]:
                return True
            else:
                if target<matrix[row][mid]:
                    r=mid-1
                elif target>matrix[row][mid]:
                    l=mid+1
                

        if(target== matrix[row][l] or  target==matrix[row][r]):
            return True
            
        return False
                

            
        
                