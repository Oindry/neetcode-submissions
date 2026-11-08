/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool Valid(TreeNode* root, long left, long right)
    {
        if (!root)
        {
            return true;
        } 
        if(!(left<root->val && root->val<right))
        {
            return false;
        }
        else
        {
            return (Valid(root->left,left,root->val)) && (Valid(root->right,root->val,right));
        }
    }
    bool isValidBST(TreeNode* root) {
        if (!root)
        {
            return true;
        } 
        return Valid(root, LONG_MIN,LONG_MAX);

    }
};
