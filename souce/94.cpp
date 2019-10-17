/*
94. Binary Tree Inorder Traversal Medium

Overview:

    Three implementations:

        1. Recursion

        2. Stack
        
            Loop: 
                
                Put cur into stack; 
                go to the most left; 
                save top and pop; 
                go to right

            until cur == NULL && stack.empty()

        3. Morris Traversal (without recursion or stack)

            Loop:
        
                if cur.left == NULL

                    save cur
                    goto right

                else

                    put cur to be the most right child of left

                    if right-most child of left is already cur

                        (recover tree)
                        set right-most child of left tobe NULL
                        save cur
                        goto right

                    else 

                        set right-most child of left tobe cur
                        goto left

            until cur == NULL
*/

/*
M1: Recursion
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
    void inorderRecur(TreeNode* root, vector<int> &res) {
        if (root == NULL) 
            return;
        inorderRecur(root->left, res);
        res.push_back(root->val);
        inorderRecur(root->right, res);
    }
    
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorderRecur(root, res);
        return res;
    }
};

/*
M2: Stack
*/

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> stackk;
        vector<int> res;
        TreeNode* cur = root;
        
        while (cur != NULL || !stackk.empty()) {
            while (cur != NULL) {
                stackk.push(cur);
                cur = cur->left;
            }
            cur = stackk.top();
            stackk.pop();
            res.push_back(cur->val);
            cur = cur->right;
        }
        return res;
    }
};

/*
M3: Morris Traversal
*/

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        TreeNode* cur = root;
        TreeNode* pre;
        
        while (cur != NULL) {
            if (cur->left == NULL) {
                res.push_back(cur->val);
                cur = cur->right;
            } else {
                pre = cur->left;
                while (pre->right != NULL && pre->right != cur)
                    pre = pre->right;
                
                if (pre->right == NULL) {
                    pre->right = cur;
                    cur = cur->left;
                } else {
                    pre->right = NULL;
                    res.push_back(cur->val);
                    cur = cur->right;
                }
            }
        }
        return res;
    }
};