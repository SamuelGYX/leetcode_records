/*
Overview:

    Given a list of array, the value in each location represents the largest step to jump. Return whether the last location is reachable from the first one.

Solution:

    A very representative dynamic programming problem. The solution part on the website provides a thorough introduction on how to come up with the final DP solution from the a naive recursive approach. I really recommend you to learn (or review) the DP mindset from it.

    > [Jump Game Solution](https://leetcode.com/problems/jump-game/solution/)

    The explanation for the final program is that we could check from the rightmost index to the leftmost and keep track of the leftmost_good position. If the leftmost_good is reachable from loc_i, then loc_i is good and loc_i becomes the new leftmost_good.
*/

class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() == 0)
            return true;
        int leftmost_good = nums.size() - 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (i + nums[i] >= leftmost_good)
                leftmost_good = i;
        }
        return leftmost_good == 0;
    }
};