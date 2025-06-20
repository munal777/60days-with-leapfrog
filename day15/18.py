class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums) - 1
        arr = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,n-1):
                if j > (i + 1) and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = n
                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]

                    if fourSum == target:
                        arr.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif fourSum > target:
                        r -= 1
                    else:
                        l += 1
        return arr