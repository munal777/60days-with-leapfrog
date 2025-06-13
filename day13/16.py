class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        threeSum = nums[0] + nums[1] + nums[2]
        if threeSum > target:
            return threeSum

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr_threeSum = nums[i] + nums[l] + nums[r]
                
                if abs(curr_threeSum - target) < abs(threeSum - target):
                    threeSum = curr_threeSum
                
                if curr_threeSum > target:
                    r -= 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_threeSum < target:
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    return target
        return threeSum
