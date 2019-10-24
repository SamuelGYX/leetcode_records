/*
40. Combination Sum II Medium

Overview: 

    Given a list of positive numbers, find all combinations whose sum is exactly equal to the positive target.

    This problem is very similar to k_sum but removes the constraints of the size of the result, i.e. only 1 number or the total list, as long as the sum is equal to the target.

Solution:

    The simplest implementation might be the recursive approach which looks like a DFS. This algorithm may be further optimized by binary search. But the current version is efficient enough for this problem setting.
*/

class Solution {
public:
    void dfs_sum(vector<int>& nums, int target, vector<int>& path, vector<vector<int>>& res, int start) {
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < nums.size() && nums[i] <= target; i++) {
            if (i != start && nums[i] == nums[i-1])
                continue;
            path.push_back(nums[i]);
            dfs_sum(nums, target-nums[i], path, res, i+1);
            path.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> path;
        vector<vector<int>> res;
        sort(candidates.begin(), candidates.end());
        dfs_sum(candidates, target, path, res, 0);
        return res;
    }
};