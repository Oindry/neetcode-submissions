class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int res=0;
        stack<int> stack;
        
        for (string s: tokens)
        {
            if(s=="+")
            {
                int i= stack.top();
                stack.pop();
                int j= stack.top();
                stack.pop();
                stack.push(i+j);
            }
            else if(s=="-")
            {
                int i= stack.top();
                stack.pop();
                int j= stack.top();
                stack.pop();
                stack.push(j-i);
            }
            else if(s=="*")
            {
                int i= stack.top();
                stack.pop();
                int j= stack.top();
                stack.pop();
                stack.push(j*i);
            }
            else if(s=="/")
            {
                int i= stack.top();
                stack.pop();
                int j= stack.top();
                stack.pop();
                stack.push(j/i);
            }
            else
            {
                stack.push(stoi(s));
            }
        }
        return stack.top();
    }
};
