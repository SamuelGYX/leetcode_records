# Solutions



## 02-15-2020



### Maximum subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

- 53 Maximum Subarray Easy

- 121 Best Time to Buy and Sell Stock Easy

Sol 1: DP

```C++
dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0)
```

Sol 2: Divide-and-Conquer



### Finite State Machine

- 309  Best Time to Buy and Sell Stock with Cooldown Medium
- 123 Best Time to Buy and Sell Stock III Hard
- 188 Best Time to Buy and Sell Stock IV Hard



### Skip and Earn

- 198 House Robber Easy
  - Compute the max sum of subarrays without adjacent elements.
- 213 House Robber II Medium
- 337 House Robber III Medium
- 740 Delete and Earn Medium
- 



### Similar DP

- 152 Maximum Product Subarray
  - Compute the max product of subarrays
- 978 Longest Turbulent Subarray
  - Turbulent means alternative signs
- 600 Non-negative Integers without Consecutive Ones Hard
  - Find the number of strings without consecutive ones



### Sum of Subarray Equals to X

- 1,Two Sum,Easy
- 167,Two Sum II - Input array is sorted,Easy
- 653,Two Sum IV - Input is a BST,Easy
- 560,Subarray Sum Equals K,Medium
- 15,3Sum,Medium
- 18,4Sum,Medium
- 



### Others

- 697 Degree of an Array Easy
  - Compute the shortest subarray containing the mode number, i.e. last index subtract first index of mode
- 122 Best Time to Buy and Sell Stock II Easy
  - Compute the sum of all positive numbers.
- 628 Maximum Product of Three Numbers Easy
- 238 Product of Array Except Self Medium
- 1 Two Sum Easy
- 167 Two Sum II - Input array is sorted Easy
- 653 Two Sum IV - Input is a BST Easy