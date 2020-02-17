'''
645. Set Mismatch
Easy

The set S originally contains numbers from 1 to n. One of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number. Your task is to firstly find the number occurs twice and then find the number that is missing.

Solution:
(see 448. Find All Numbers Disappeared in an Array & 268. Missing Number)

	1. Negative sign mark

	2. += (n+1) mark

	3. swap mark

	4. computation (similar to the summation method)

		act_sum - dup + mis = exp_sum 							=> diff
		act_sum_of_square - dup^2 + mis^2 = exp_sum_of_square 	=> summ * diff
			because dup^2 - mis^2 = (dup + mis)(dup - mis)
'''

class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i, v in enumerate(nums):
            v = abs(v)
            if nums[v-1] < 0:
                dup = v
            else:
                nums[v-1] *= -1
        for i, v in enumerate(nums):
            if v > 0:
                mis = i+1
        return [dup, mis]

class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.append(0)
        n = len(nums)
        for i, v in enumerate(nums):
            v %= n
            if nums[v] >= n:
                dup = v
            else:
                nums[v] += n
        for i, v in enumerate(nums):
            if v < n:
                mis = i
        return [dup, mis]

class Solution3:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i, v in enumerate(nums):
            while i != v-1:
                if nums[v-1] == v:
                    dup = v
                    break
                else:
                    nums[v-1], nums[i], v = nums[i], nums[v-1], nums[v-1]
        for i, v in enumerate(nums):
            if i+1 != v:
                mis = i+1
        return [dup, mis]

class Solution4:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        exp_sum, exp_ss = (1+n)*n//2, sum(i*i for i in range(1,n+1))
        act_sum, act_ss = sum(nums), sum(i*i for i in nums)
        diff = act_sum - exp_sum
        summ = (act_ss - exp_ss) // diff
        return [(summ + diff) // 2, (summ - diff) // 2]