# 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha_sen = ""
        for i in s: 
            if i.isalpha():
                alpha_sen += i.lower()
            if i.isnumeric():
                alpha_sen += i
        
        l = 0
        r = len(alpha_sen) - 1

        while l < r:
            if alpha_sen[l] != alpha_sen[r]:
                return False
            l += 1
            r -= 1
        return True
        # valid_s = ""
        
        # for char in s:
        #     if char.isalpha():
        #         valid_s += char.lower()
        #     if char.isnumeric():
        #         valid_s += char
        # return True if valid_s[0:len(valid_s)] == valid_s[::-1] else False
