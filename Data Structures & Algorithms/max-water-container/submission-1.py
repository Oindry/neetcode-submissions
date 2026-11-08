class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxList=[]
        for index,val in enumerate(heights):
            j=index+1
            List=[]
            maxArea=0
            while j<len(heights):
                if val<heights[j]:
                    area= val*(j-index)
                else:
                    area= heights[j]*(j-index)
                print(area)
                if maxArea<area:
                    maxArea=area
                j=j+1
            maxList.append(maxArea)
        return max(maxList)   
         

                

            
            
        