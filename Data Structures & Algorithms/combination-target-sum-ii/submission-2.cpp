
class Solution {
public:
void dfs(int i, int target,vector<int>& nums,vector<int>& sub,set<vector<int>>& res )
    {
        if(i==nums.size())
        {  
            if(target==0)
            {
                res.insert(sub);
            } 
            return;
        }
            sub.push_back(nums[i]);
            dfs(i+1,target-nums[i],nums,sub,res);
            sub.pop_back();
            dfs(i+1,target,nums,sub,res);
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        set<vector<int>> res;
        vector<int> sub;
        sort(candidates.begin(), candidates.end());
        dfs(0,target,candidates,sub,res);
        return vector<vector<int>>(res.rbegin(),res.rend());
    }
};
