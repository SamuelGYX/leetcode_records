/*

102. [Binary Tree Level Order Traversal]

(https://leetcode.com/problems/binary-tree-level-order-traversal/) 

Medium

*/

/*

Overview: 
    A very easy problem about BFS, the only difference from basic BFS is:
        put nodes into seperate vectors according to their level.

    This requirement could be fulfilled by using another queue recording the levels of the corresponding nodes in node_Q.

Additions:

    vector `=` is treated as copy-by-value.

    > std::vector::operator=
    > 
    > Assigns new contents to the container, replacing its current contents, and modifying its size accordingly.
    > 
    > Ref: http://www.cplusplus.com/reference/vector/vector/operator=/

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (root == NULL) {
            return res;
        }
        vector<int> tmpV;
        int recLv = -1;
        
        queue<TreeNode *> trQ;
        queue<int> lvQ;
        trQ.push(root);
        lvQ.push(0);
        while (!trQ.empty()) {
            TreeNode * curTr = trQ.front();
            trQ.pop();
            int curLv = lvQ.front();
            lvQ.pop();
            
            if (recLv < curLv) {
                res.push_back(tmpV);
                recLv = curLv;
            }
            
            res[recLv].push_back(curTr->val);
            
            if (curTr->left != NULL) {
                trQ.push(curTr->left);
                lvQ.push(recLv + 1);
            }
            if (curTr->right != NULL) {
                trQ.push(curTr->right);
                lvQ.push(recLv + 1);
            }
        }
        
        return res;
    }
};