# Find Closest Number to Zero

## Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

class Solution: 
    def findClosestNumber(self, nums: List[int]) -> int:
        min=float('inf')
        nums.sort()
        for val in nums:
            if abs(val) <= abs(min):
                min = val
        return min

obj = Solution()

# Example 1
nums = [2,5,1,-1,4,7]
print(obj.findClosestNumber(nums))


