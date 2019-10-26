/**
 * Overview:
 *
 * 		Given a binary tree, transform it into a linked list linked on 'right'
 * 		in preorder sequence.
 *
 * Solution:
 *
 * 		1. Naive recursion
 *
 * 			This is a more straightforward solution come up by myself. Flatten 
 * 			right and left children (sequence does not matter), then insert 
 * 			the left subtree within the root and right subtree. 
 *
 * 		2. Improved recursion
 *
 * 			This is the solution referenced from the 'Discuss' section. The 
 * 			first part is the same: Flatten right and left children. But, this 
 * 			time, the sequence cannot be altered. Then, with the help of a 
 * 			global variable, we could store the previous root and do not need 
 * 			to find the left_rightmost with loops.
 *
 * 			Suppose the initial tree looks like this:
 *
 * 			   1
 *			 2   5
 * 			3 4   6
 *
 * 			After recursive calls of flatten on 1->right (i.e. 5), the first 
 * 			backtrack happens at root=6, pre_root=NULL. Then, we backtrack to 
 * 			root=5, pre_root=6 and set 5->right = 6 and pre_root = 5.
 *
 * 			After that, another recursive call on 1->left (i.e. 2). the first 
 * 			backtrack happens at root=4, pre_root=5 and we set 4->right = 5, 
 * 			pre_root = 4. This is the most important step.
 *
 * 			Finally, we will backtrack on 3, 2, and back to 1. Finish flatten.
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

/**
 * Naive recursion
 */

class Solution {
public:
    void flatten(TreeNode* root) {
        if (root == NULL)
            return;
        flatten(root->right);
        flatten(root->left);
        
        TreeNode* left_rightmost = root->left;
        if (left_rightmost == NULL)
            return;
        while (left_rightmost->right != NULL)
            left_rightmost = left_rightmost->right;
        
        left_rightmost->right = root->right;
        root->right = root->left;
        root->left = NULL;
    }
};

/**
 * Improved recursion
 */

class Solution {
public:
    TreeNode* pre_root = NULL;

    void flatten(TreeNode* root) {
        if (root == NULL)
            return;
        flatten(root->right);
        flatten(root->left);
        root->right = pre_root;
        root->left = NULL;
        pre_root = root;
    }
};