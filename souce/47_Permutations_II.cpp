/*
47. Permutations II Medium

Overview:

    Given a list of numbers with duplication, return all unique permutations.

Solution:

    Implement nested loop with recursion. Select an unused number in each layer of loop (recursion). Similar to DFS.

    Avoid duplicate results by sorting and enforcing the sequence of selecting duplicates (i.e. cannot select the latter ones until the former one is picked). This means we do not exchange the order of the same numbers.
*/

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> res;
        vector<bool> used(nums.size(), false);
        sort(nums.begin(), nums.end());
        dfs(nums, path, res, used);
        return res;
    }
    
    void dfs(vector<int>& nums, vector<int>& path, vector<vector<int>>& res, vector<bool>& used) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (used[i])
                continue;
            if (i > 0 && nums[i] == nums[i-1] && !used[i-1])
                continue;
            used[i] = true;
            path.push_back(nums[i]);
            dfs(nums, path, res, used);
            used[i] = false;
            path.pop_back();
        }
    }
};