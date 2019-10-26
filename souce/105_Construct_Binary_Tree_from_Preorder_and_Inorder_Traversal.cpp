/**
 * Overview:
 *
 *      Given preorder and inorder traverse, reconstruct the binary tree.
 *
 * Solution:
 *
 *      This problem looks concerned with recursion. 
 *
 *      preorder:   [root left right]
 *      inorder:    [left root right]
 *
 *      Thus, we could find use the first element in preorder to divide 
 *      inorder into two parts: left and right. Then, use the next element in 
 *      preorder further divide the left subtree and then right subtree.
 *
 * Tricky point:
 *
 *      1. Remember to decrement pre_loc when the root element in preorder is 
 *      unused.
 *
 *      2. Allocating memory space with `new` in C++ is like `malloc` in C.
 *
 *      > [malloc() vs new](https://www.geeksforgeeks.org/malloc-vs-new/)
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
    TreeNode* subTree(vector<int>& preorder, vector<int>& inorder, 
        int& pre_loc, int in_start, int in_end) {
        if (pre_loc >= preorder.size() || in_start > in_end) {
            pre_loc--;
            return NULL;
        }
        
        for (int i = in_start; i <= in_end; i++) {
            if (inorder[i] == preorder[pre_loc]) {
                TreeNode* tn = new TreeNode(inorder[i]);
                tn->left = subTree(preorder, inorder, 
                    ++pre_loc, in_start, i-1);
                tn->right = subTree(preorder, inorder, 
                    ++pre_loc, i+1, in_end);
                return tn;
            }
        }
        return NULL;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty())
            return NULL;
        int pre_loc = 0;
        return subTree(preorder, inorder, pre_loc, 0, inorder.size()-1);
    }
};