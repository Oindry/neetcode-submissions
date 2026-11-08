class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        std::unordered_map<char,char> closeToOpen= {
            {')','('},
            {']','['},
            {'}','{'}
        };

        for(char c: s)
        {
            if(closeToOpen.count(c))
            {
                if(stack.empty() or stack.top()!=closeToOpen[c])
                {
                    return false;
                }
                else
                {
                    stack.pop();
                }
            }
            else
            {
                stack.push(c);
            }
        }
        return stack.empty();
    }
};
