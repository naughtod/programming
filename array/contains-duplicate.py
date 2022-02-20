class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        O(nlogn) solution
        """
        
        nums.sort()
        i = 1
        
        while i < len(nums) and nums[i-1] != nums[i]:
            i += 1
            
        return True if i < len(nums) else False
