class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> hashmap;
        vector<int> res;

        for(int i=0; i<nums.size(); i++)
        {
            int remain= target-nums[i];
            if(hashmap.count(remain))
            {
                res.push_back(hashmap[remain]);
                res.push_back(i);
                return res;
            }
            hashmap[nums[i]]=i;
        }
        return {};
        
    }
};
