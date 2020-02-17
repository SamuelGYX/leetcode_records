'''

'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        take = skip = 0
        for k in sorted(cnt):
            take, skip = k*cnt[k] + (skip if cnt[k-1] else max(take, skip)), max(take, skip)
        return max(take, skip)