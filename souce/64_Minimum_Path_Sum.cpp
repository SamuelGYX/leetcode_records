/*
Overview:

    An easy DP problem.
*/

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.empty())
            return 0;
        vector<int> memo(grid[0]);
        for (int j = 1; j < memo.size(); j++)
            memo[j] += memo[j-1];
        for (int i = 1; i < grid.size(); i++) {
            memo[0] += grid[i][0];
            for (int j = 1; j < memo.size(); j++)
                memo[j] = min(memo[j-1], memo[j]) + grid[i][j];
        }
        return memo[memo.size()-1];
    }
};