class Solution {
public:
    int characterReplacement(string s, int k) {
       int l=0;
       int r=0;
       unordered_map<char,int> freq;
       int maxF=0;
       int res=0;
       while(r!=s.size())
       {
            freq[s[r]]++;
            maxF= max(maxF,freq[s[r]]);
            while((r-l+1)-maxF>k)
            {
                freq[s[l]]--;
                l++;
            }

            res= max(res,r-l+1);
            r++;
       }
       return res;

    }
};
