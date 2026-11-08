class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash=defaultdict(int)
        max_value=0

        
        for i in nums:
            if not hash[i]:
                hash[i]=hash[i-1]+hash[i+1]+1
                hash[i-hash[i-1]]= hash[i]
                hash[i+hash[i+1]]= hash[i]
                max_value=max(max_value,hash[i])

            
            
           

        
        return max_value
        
                
                    
        

        