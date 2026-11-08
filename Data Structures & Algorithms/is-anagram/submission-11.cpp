class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> s_map;
        map<char,int> t_map;
        for (char c: s)
        {
            if (s_map.count(c))
            {
                s_map[c]= s_map[c]+1;
            }
            else
            {
                s_map[c]=1;
            }
        }
        for (char c: t)
        {
            if (t_map.count(c))
            {
                t_map[c]= t_map[c]+1;
            }
            else
            {
                t_map[c]=1;
            }
        }

        if (s_map==t_map)
        {
            return true;
        }
        return false;


    }
};
