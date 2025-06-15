class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_avg = float('-inf')
        start = 0
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            avg = current_sum/ float(k)

            if (i - start + 1) == k:
                max_avg = max(max_avg, avg)
                current_sum -= nums[start]
                start += 1
        
        return max_avg