class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table= dict()
        my_dict=dict()
        for i in nums:
            if i in hash_table:
                hash_table[i]+=1
                
            else:
                hash_table[i]=1
            
        my_dict= hash_table
        ans= []
        for i in range(k):
            for key,value in hash_table.items():
           
                max_value= max(my_dict.values())
                if value==max_value:
                    ans.append(key)
                    my_dict.pop(key)
                    break
            
        return ans

        
            

