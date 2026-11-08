class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r=0,len(nums)-1
        i=-1
        while l<=r:
                m= l+(r-l)//2
                if target== nums[m]:
                    i=m
                    break
                elif target==nums[l]:
                    i=l
                    break
                elif target== nums[r]:
                    i=r
                    break
                else:
                    if nums[m]>=nums[l]:
                        if nums[l]<target<nums[m]:
                            r=m-1
                        else:
                            l=m+1
                    else:
                        r=m-1
        return i
            

            

        
                    
                


