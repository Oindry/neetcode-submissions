class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l1=0;
        int r1= matrix.size()-1;
       
        vector<int> targetMatrix;
        while(l1<=r1)
        {
            int mid1= l1+((r1-l1)/2);
            if(matrix[mid1][0]<=target && matrix[mid1][matrix[mid1].size()-1]>=target)
            {
                targetMatrix=matrix[mid1];
                break;
            }
            else
            {
                if(matrix[mid1][0]>target)
                {
                    r1= mid1-1;
                }
                if(matrix[mid1][matrix[mid1].size()-1]<target)
                {
                    l1=mid1+1;
                }
            }
        }
        if (targetMatrix.empty()) return false;
        int l=0;
        int r=targetMatrix.size()-1;
        
        while(l<=r)
        {
            int mid= l+((r-l)/2);
            
            if(targetMatrix[mid]==target)
            {
                return true;
            }
            else
            {
                if(targetMatrix[mid]>target)
                {
                    r=mid-1;
                }
                if(targetMatrix[mid]<target)
                {
                    l=mid+1;
                }
            }
        }
        
        
        return false;
    }
};
