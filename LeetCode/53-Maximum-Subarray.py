# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(self, nums):
        
        output = []
        temp = 0
        
        for num in nums:
            temp += num
            if num > temp:
                temp = num
            output.append(temp)

        return max(output)

obj = Solution()

print(obj.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))