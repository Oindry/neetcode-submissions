class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prevdic= {} #Value->Index
      for i,n in enumerate(nums):
        diff= target-n
        if diff in prevdic:
            return [prevdic[diff],i]
        prevdic[n]= i
        
                        
                

           
            

                

        
        