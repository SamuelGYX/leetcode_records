'''
442. Find All Duplicates in an Array
Medium

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once. Find all the elements that appear twice in this array.

Time: O(n), Space: O(1)

Solution:

	1. Negative mark

	2. += n mark

	3. Swap mark

		Two methods for break loop: 1. loop until current position is correct OR 2. loop until the target is correct. The succeed code should also be modified. 
'''
class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i, v in enumerate(nums):
            if nums[abs(v)-1] < 0:
                ans.append(abs(v))
            else:
                nums[abs(v)-1] *= -1
        return ans

class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.append(0)
        ans, n = [], len(nums)
        for i, v in enumerate(nums):
            if nums[v%n] >= n:
                ans.append(v%n)
            else:
                nums[v%n] += n
        return ans

class Solution3:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        for i, v in enumerate(nums):
            while v != i+1: 		# OR while nums[v-1] != v:
                if nums[v-1] == v:
                    ans.add(v)
                    break
                else:
                    nums[v-1], nums[i], v = nums[i], nums[v-1], nums[v-1]
        return list(ans)
