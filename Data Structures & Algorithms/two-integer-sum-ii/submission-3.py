class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash=defaultdict(int)

        for index,val in enumerate(numbers):
            remain= target-val
            if remain in hash:
                return [ hash[remain], index+1]
            
            hash[val]=index+1
        