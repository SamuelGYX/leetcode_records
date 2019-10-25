/*
Overview:

    Given an array of distinct integers, return all combinations.

Solution:

    This problem is very easy given the elements are distinct. We just need to do a recursion and get all possible combinations. Remember to push and pop before each recursive function call.

    After all, there is a summary of backtracking questions in the Discuss section as attached below. I believe it is a very valuable reference for similar problems.

    [A general approach to backtracking questions in Java (Subsets, Permutations, Combination Sum, Palindrome Partitioning)](https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning))
*/

class Solution {
public:
    void dfs(vector<int>& nums, vector<int>& path, vector<vector<int>>& res, int start) {
        if (start == nums.size()) {
            res.push_back(path);
            return;
        }
        path.push_back(nums[start]);
        dfs(nums, path, res, start+1);
        path.pop_back();
        dfs(nums, path, res, start+1);
    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> res;
        dfs(nums, path, res, 0);
        return res;
    }
};