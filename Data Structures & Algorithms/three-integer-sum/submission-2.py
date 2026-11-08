class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_Trip=[]
        nums.sort()
        processed=[]
        for i in range(len(nums)):
            if nums[i] not in processed:
                l,r= i+1,len(nums)-1
                while l<r:
                    if nums[i]+nums[l]+nums[r]==0:
                        if([nums[i],nums[l],nums[r]] not in my_Trip):
                            my_Trip.append([nums[i],nums[l],nums[r]])
                        l=l+1
                        r=r-1
                    elif nums[i]+nums[l]+nums[r]>0:
                        r=r-1
                    elif nums[i]+nums[l]+nums[r]<0:
                        l=l+1
        return (my_Trip)
        
            



        