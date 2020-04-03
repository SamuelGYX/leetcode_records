'''
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. No duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.kSum(sorted(nums), 0, 3, 0)
    
    def kSum(self, nums, t, k, s):
        if s > len(nums)-k:
            return []
        if k == 2:
            return self.twoSum(nums, t, s)
        out, pre_v = [], None
        for i, v in enumerate(nums[s:]):
            if v == pre_v:
                continue
            part, pre_v = self.kSum(nums, t-v, k-1, s+i+1), v
            for p in part:
                out.append([v] + p)
        return out

    def twoSum(self, nums, t, s):
        l, r, out = s, len(nums)-1, []
        while l < r:
            s = nums[l] + nums[r]
            if s < t:
                l += 1
            elif s > t:
                r -= 1
            else:
                if not out or out[-1] != [nums[l], nums[r]]:
                    out.append([nums[l], nums[r]])
                l, r = l+1, r-1
        return out