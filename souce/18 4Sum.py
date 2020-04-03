'''
18. 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target. No duplicate quadruplets.
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(sorted(nums), target, 4, 0)
        
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