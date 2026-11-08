class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        myList=[]
        for l in range(len(nums)):
            r=l+1
            while r<=(len(nums)-1):
                if(nums[l]+nums[r]== target):
                    myList.append(l)
                    myList.append(r)
                    return myList       
                else:
                    r+=1
                    
            

