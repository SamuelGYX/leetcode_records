/*
Overview:
    Given an array of 0, 1, and 2. Return the sorted one.
Solution:
    A special sort algorithm for elements with 3 types. Keep a reference to the begin and end location of unsorted area (i.e. area of 1) and scan the unsorted part. If the number is 0 or 2, do swap.
Tricky point:
    Increment and decrement conditions of three pointers are very prone to errors.
*/

class Solution {
public:
    void sortColors(vector<int>& nums) {
        if (nums.size() <= 1)
            return;
        int begin_1 = 0, end_1 = nums.size()-1;
        for (int i = begin_1; i <= end_1; i++) {
            if (nums[i] == 0 && i > begin_1)
                swap(nums[begin_1++], nums[i--]);
            else if (nums[i] == 2 && i < end_1) {
                swap(nums[end_1--], nums[i--]);
            }
        }
        return;
    }
};