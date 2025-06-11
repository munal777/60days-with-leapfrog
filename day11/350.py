# 350. Intersection of Two Arrays II

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        seen = {}
        result = []
        for num in nums1:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        for num in nums2:
            if num in seen:
                if seen[num] > 0:
                    result.append(num)
                seen[num] -= 1
        
        return result

obj = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(obj.intersect(nums1, nums2))