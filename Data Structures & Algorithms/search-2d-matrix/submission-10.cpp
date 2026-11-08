class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l1 = 0;
        int r1 = matrix.size() - 1;

        vector<int> targetMatrix;

        while (l1 <= r1) // changed from l1 < r1 to l1 <= r1 to include last row
        {
            int mid1 = l1 + ((r1 - l1) / 2);

            // Handle exact match at start or end of row
            if (matrix[mid1][0] <= target && matrix[mid1][matrix[mid1].size() - 1] >= target)
            {
                targetMatrix = matrix[mid1];
                break; // found the correct row, exit loop
            }
            else
            {
                if (matrix[mid1][0] > target)
                {
                    r1 = mid1 - 1;
                }
                else if (matrix[mid1][matrix[mid1].size() - 1] < target)
                {
                    l1 = mid1 + 1;
                }
            }
        }

        if (targetMatrix.empty()) return false; // in case no row is selected

        int l = 0;
        int r = targetMatrix.size() - 1;

        // cout << targetMatrix[l]; // optional for debugging

        while (l <= r) // changed from l < r to l <= r
        {
            int mid = l + ((r - l) / 2);

            // cout << targetMatrix[mid]; // optional for debugging

            if (targetMatrix[mid] == target)
            {
                return true;
            }
            else
            {
                if (targetMatrix[mid] > target)
                {
                    r = mid - 1; // fixed wrong direction
                }
                else
                {
                    l = mid + 1; // fixed wrong direction
                }
            }
        }
        return false;
    }
};