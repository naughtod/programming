class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, max = 0, 0
        
        for i in range(len(s)):
            for j in range(start, i):
                if s[i] == s[j]:
                    start = j+1
            
            if i-start+1 > max:
                max = i-start+1
            
        return max
