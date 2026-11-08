class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int i=0;
        vector<int> res;
        while(i<nums.size())
        {
            int j=0;
            int prod=1;
            cout<<prod;
            while(j<nums.size())
            {
                if(j!=i)
                {
                    prod=prod*nums[j];
                }
                j++;
            }
            res.push_back(prod);
            i++;
        }
        return res;
    }
};
