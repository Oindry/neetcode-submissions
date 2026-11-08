class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashmap;
        vector<int> output;
        for (int i=0;i<nums.size();i++)
        {
            int remain= target- nums[i];
            if(hashmap.count(remain))
            {
                output.push_back(hashmap[remain]);
                output.push_back(i); 
                return output;
            }
            hashmap[nums[i]]= i;
            
        }
        return {};
        
    }
};
