# 349. Intersection of Two Arrays

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2 = list(set(nums2))
        result = []

        for i in nums2:
            l = 0
            r = len(nums1) - 1
            while l <= r:
                mid = (r+l)//2
                if nums1[mid] == i:
                    result.append(i)
                    break
                elif nums1[mid] > i:
                    r = mid - 1
                elif nums1[mid] < i:
                    l = mid + 1
        return result

obj = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(obj.intersection(nums1, nums2))