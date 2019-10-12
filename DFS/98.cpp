/*

98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
Medium

*/

/*

Overview:
    
    Simple DFS problem

Tricky points: 
    
    one input is the maximum value of int (i.e. 0x7fffffff, 2147483647). Setting INF as `long` resolves this problem.

    p.s. 0x3f3f3f3f is equal to 1061109567

*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    const long INF = 0x3f3f3f3f3f3f3f3f;
    
    bool isValidBSTRecur(TreeNode* root, long low, long high) {
        if (root == NULL) {
            return true;
        }
        
        if (root->val <= low || root->val >= high) {
            return false;
        }
        
        if (isValidBSTRecur(root->left, low, root->val) 
            && isValidBSTRecur(root->right, root->val, high)) {
            return true;
        } else {
            return false;
        }
    }
    
    bool isValidBST(TreeNode* root) {
        return isValidBSTRecur(root, -INF, INF);
    }
};