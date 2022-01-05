# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

nums = [3,3]
target = 6

class Solution:
    def twoSum(self, nums, target):
        index = 1
        for element1 in range(len(nums)):
            for element2 in range(index,len(nums)):
                tmp_target = nums[element1] + nums[element2]
                if tmp_target == target:
                    return [element1,element2]
                    exit()
            index += 1

obj = Solution()

print(obj.twoSum(nums=[3,3],target=6))