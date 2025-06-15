class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0 
        maxs = 0
        sumed = 0
        sets = set()

        for r in range(len(nums)):
            while nums[r] in sets:
                sets.remove(nums[l])
                sumed -= nums[l]
                l += 1
            sets.add(nums[r])
            sumed += nums[r]

            if r-l + 1 == k:
                maxs = max(sumed,maxs)
                sumed -= nums[l]
                sets.remove(nums[l])
                l += 1
        return maxs