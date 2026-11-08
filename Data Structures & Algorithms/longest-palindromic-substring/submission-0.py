class Solution:
    def longestPalindrome(self, s: str) -> str:
        #This stores the the starting ponter of the longest palindrome
        resIndex=0
        #This stores the longest length
        reslength=0

        for i in range(len(s)):
            #odd case
            l,r=i,i
            #check bounds and if palindrome
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                #check if result needs to be updated
                if(reslength<(r - l + 1)):
                    resIndex=l
                    reslength=r - l + 1
                l-=1
                r+=1

            #Even case
            l,r=i,i+1
            #check bounds and if palindrome
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                #check if result needs to be updated
                if(reslength<(r - l + 1)):
                    resIndex=l
                    reslength=r - l + 1
                l-=1
                r+=1

        return s[resIndex: resIndex+reslength]


                
        
        