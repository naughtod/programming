class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        O(n) solution, does not use divide
        """
        
        forward, backward, result = [], [], []
        f_num, b_num = 1, 1
        
        for i in range(len(nums)):
            f_num *= nums[i]
            forward.append(f_num)
            
            b_num *= nums[-i-1]
            backward.append(b_num)
        
        backward = backward[::-1]
        
        result.append(backward[1])
        
        for i in range(len(nums)-2):
            result.append(forward[i]*backward[i+2])
            
        result.append(forward[len(nums)-2])
        
        return result
