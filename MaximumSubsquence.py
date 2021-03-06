class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_and = nums[0] 
        max_ = current_and
        for i in range(1,len(nums)):
            if current_and > 0 :
                max_ = max(max_,current_and+nums[i])
                current_and = current_and + nums[i]
            else:
                max_ = max(max_,current_and,nums[i])
                current_and = nums[i]
        return max_