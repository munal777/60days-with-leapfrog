class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            if i > 0 and (nums[i] == nums[i - 1]):
                continue

            first = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sec = nums[l]
                last = nums[r]
                sum = first + sec + last
                if sum == 0:
                    result.append([first,sec,last])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
                    
        return result