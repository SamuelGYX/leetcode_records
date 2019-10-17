/*
18. 4Sum Medium

Overview:

    Find combinations in a given array whose sum is equal to target.

    Solution: Recursion

    Divide the problem into sub-problems until simple 2-sum problem. Remember to jump over duplicate values in order to eliminate duplicate combinations.
*/

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        return kSum(nums, target, 4, 0);
    }
    
    vector<vector<int>> kSum(vector<int>& nums, int target, int k, int start) {
        vector<vector<int>> res, tempRes;
        if (start >= nums.size())
            return res;
        
        if (k == 2) {
            int i = start, j = nums.size() - 1, sum;
            while (i < j) {
                sum = nums[i] + nums[j];
                if (sum < target) {
                    i++;
                } else if (sum > target) {
                    j--;
                } else {
                    res.push_back(vector<int>{nums[i], nums[j]});
                    while (i+1 < j && nums[i+1] == nums[i])
                        i++;
                    while (i < j-1 && nums[j-1] == nums[j])
                        j--;
                    i++;
                    j--;
                }
            }
        } else {
            for (int i = start; i < nums.size(); i++) {
                
                tempRes = kSum(nums, target-nums[i], k-1, i+1);
                if (!tempRes.empty()) {
                    for (int j = 0; j < tempRes.size(); j++) {
                        tempRes[j].push_back(nums[i]);
                        res.push_back(tempRes[j]);
                    }
                }
                
                while (i+1 < nums.size() && nums[i+1] == nums[i])
                    i++;
            }
        }
        return res;
    }
};