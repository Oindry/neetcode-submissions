class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       int l=0;  int r=0;
       unordered_set<char> track;
       int count=0;

       while(r<s.size()){
        while(track.find(s[r])!= track.end()) // this means, s[r], has been found prior end of track;
        {
            track.erase(s[l]);
            l++;
        }
        track.insert(s[r]);
        count= max(count, r-l+1);
        r++;

       }
       return count;

    }
};
