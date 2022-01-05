#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution: 
    def shuffle(self, nums, n):
        return reduce(lambda a, b: a + b, [[nums[i], nums[j]] for i, j in zip(range(0, n), range(n, 2 * n))])

obj = Solution()

# Example 1
nums = [2,5,1,3,4,7]
n = 3

print(obj.shuffle(nums,n))
