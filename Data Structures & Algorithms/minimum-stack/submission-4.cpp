class MinStack {
public:
    std::stack<int> stack;
    std::stack<int> min;

    
    void push(int val) {
        stack.push(val);
        if(min.empty())
        {
            min.push(val);
        }
        else
        {
            int i= min.top();
            if (i>val)
            {
                min.push(val);
            }
            else
            {
                min.push(i);
            }
            
        }
        
    }
    
    void pop() {
        stack.pop();
        min.pop();

    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return min.top();
    }
};
