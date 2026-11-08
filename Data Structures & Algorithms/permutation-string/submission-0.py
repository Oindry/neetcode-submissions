class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count=[0]*26
        for c in s1:
            index= ord(c)-ord("a")
            s1count[index]+=1
        

        s2count=[0]*26
        left=0
        for right in range(len(s2)):
            index= ord(s2[right])-ord("a")
            s2count[index]+=1
            if right - left + 1 > len(s1):
                left_Index= ord(s2[left])-ord("a")
                s2count[left_Index]-=1
                left=left+1
            if(s1count==s2count):
                return True

            
        return False

        



            

        