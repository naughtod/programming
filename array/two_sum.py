class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        O(nlogn) solution, sort and then scan from outside in
        """
        nums_args = sorted(range(len(nums)), key=nums.__getitem__)
        nums.sort()
           
        ind_1 = 0
        ind_2 = len(nums)-1
        num_sum = nums[ind_1] + nums[ind_2]
        
        while num_sum != target:
            if num_sum < target: ind_1 += 1 
            else: ind_2 -= 1
            num_sum = nums[ind_1] + nums[ind_2]
            
        
        return [nums_args[ind_1], nums_args[ind_2]]
        
                
        
