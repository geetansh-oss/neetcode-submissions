class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        suffix = 1

        #currently we have stored the prefix multiplication of the index in res
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        for i in range(len(nums) - 1 , -1, -1):
            res[i] = suffix * res[i]
            suffix *= nums[i]

        return res