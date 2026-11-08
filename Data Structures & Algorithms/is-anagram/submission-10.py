class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict=defaultdict(int)
        t_dict=defaultdict(int)
        same= True
        if(len(s)!=len(t)):
            return False
        else:
            for i in s:
                s_dict[i]=s_dict.get(i,0)+1
            for i in t:
                t_dict[i]=t_dict.get(i,0)+1
            
            for key, val in s_dict.items():
                if t_dict[key]!=val:
                    same= False
        return same


        