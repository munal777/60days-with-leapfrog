# 287. Find the Duplicate Number

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = 0
 
        while l < len(nums)-1:
            r = l + 1
            if nums[l] == nums[r]:
                return nums[l]
            else:
                l += 1

obj = Solution()
nums = [1,3,4,2,2]
print(obj.findDuplicate(nums))