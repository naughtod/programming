class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        O(n) solution
        """
        
        ind_1, ind_2 = 0, 0
        sub_sum, max_sum = nums[0], nums[0]
        
        for i in range(len(nums)-1):
            
            if sub_sum <= 0:
                ind_1 = i+1
                ind_2 = i+1
                sub_sum = nums[ind_1]
            else :
                ind_2 += 1
                sub_sum += nums[ind_2]
                
            if sub_sum > max_sum:
                max_sum = sub_sum
        
        return max_sum
