class Solution {
public:

    void backTrack(int i,vector<bool>& pick,vector<int>& nums,vector<int>& sub, vector<vector<int>>& res )
    {
        if(sub.size()==nums.size())
        {
            res.push_back(sub);
            return;
        }
        for(int i=0; i<nums.size(); i++)
        {
            if(!pick[i])
            {
                pick[i]=true;
                sub.push_back(nums[i]);
                backTrack(i,pick,nums,sub,res);
                pick[i]=false;
                sub.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> sub;
        vector<bool> pick(nums.size(),false);
        backTrack(0,pick,nums,sub,res);
        return res;
    }
};
