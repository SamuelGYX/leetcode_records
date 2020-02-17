'''
287. Find the Duplicate Number
Medium

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), assume that there is only one duplicate number (may duplicate for many times), find the duplicate one.

Time: O(n), Space: O(1), *No modification*

Solution:

	If we treat the array as a linked list where index points to values, the duplicate number must been pointed multiple times resulting in a loop or dead end. Then we could apply the technique of finding a circle in linked list to solve this problem. (see 142. Linked List Cycle II)

	Example:

	index	0 1 2 3 4 5
	value 	3 2 4 1 1 5

                         +-------> 2M
                         |
                         +         +
                                   |
    0S +-----> 3 +-----> 1E        |		and 5
                                   |
                         ^         v
                         |
                         +-------+ 4

	Tricky point:

		return entry (i.e. 1) instead of nums[entry] (i.e. nums[1])

		If modification is allowed, we could apply special mark methods. (see 448. Find All Numbers Disappeared in an Array)
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        entry = 0
        while entry != slow:
            slow, entry = nums[slow], nums[entry]
        return entry