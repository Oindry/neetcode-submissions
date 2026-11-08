class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans= defaultdict(list)

        for obj in strs:
            count= [0]*26
            for ch in obj:
                count[ord(ch)-ord("a")]+=1
            ans[tuple(count)].append(obj)

        return ans.values()
        