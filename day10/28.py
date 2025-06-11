# 28. Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)

        for i in range(0,len(haystack)-n+1):
            strs = haystack[i:n+i]
            if strs == needle:
                return i
        return -1