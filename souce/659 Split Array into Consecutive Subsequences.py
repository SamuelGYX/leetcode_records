'''
Overview:
    
    Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Solutions:

    Greedy approach. left[i] means how many numbers of i does not participated in any sequence. end[i] means how many sequences end at number i.
'''

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]:
                continue
            left[i] -= 1
            if end[i-1]:
                end[i-1] -= 1
                end[i] += 1
            elif left[i+1] and left[i+2]:
                left[i+1] -= 1
                left[i+2] -= 1
                end[i+2] += 1
            else:
                return False
        return True