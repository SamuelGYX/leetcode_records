/*
16. 3Sum Closest Medium

Overview:

    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.

    Sort the array and use 3 pointers to loop each combinations.

Tricky points:

    Initialize res (closest sum) with an arbitrary combination. Just picking an arbitrary value (like 0) will resulted in errors.
*/

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.size(); i++) {
            int j = i + 1, k = nums.size() - 1;
            while (j < k) {
                int cur_sum = nums[i] + nums[j] + nums[k];
                int diff = cur_sum - target;
                cout << cur_sum << ' ' << diff << endl;
                
                if (diff > 0) {
                    k--;
                } else if (diff < 0) {
                    j++;
                } else {
                    return cur_sum;
                }
                
                if (abs(diff) < abs(res - target)) {
                    res = cur_sum;
                }
            }
        }
        return res;
    }
};