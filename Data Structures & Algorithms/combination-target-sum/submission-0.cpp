class Solution {
public:
    void dfs(int i, int target,vector<int>& nums,vector<int>& sub,vector<vector<int>>& res )
    {
        if(i==nums.size())
        {  
            if(target==0)
            {
                res.push_back(sub);
            } 
            return;
        }
        if(nums[i]<=target)
        {
            sub.push_back(nums[i]);
            dfs(i,target-nums[i],nums,sub,res);
            sub.pop_back();
        }
        dfs(i+1,target,nums,sub,res);
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> sub;
        dfs(0,target,nums,sub,res);
        return res;
    }
};
