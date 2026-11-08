class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> store(nums.begin(),nums.end());
        int longest=0;
        for (int num:nums)
        {
            int streak=0;
            int curr=num;
            while(store.find(curr)!= store.end())
            {
                curr++;
                streak++;
            }
            longest= max(longest,streak);
        }
        return longest;
    }
};
