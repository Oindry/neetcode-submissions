class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr= []
        for i in nums:
            print(arr)
            print (i)
            if i in arr:
                return i  
            else:
                arr.append(i)

