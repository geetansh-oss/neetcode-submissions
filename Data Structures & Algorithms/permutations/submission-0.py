class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        subset = []
        res = []
        flag = [0] * len(nums) 

        def permutation(nums):
            if len(subset) == len(nums):
                res.append(subset[::])
                return
            for i in range(len(nums)):
                if flag[i] == 0:
                    subset.append(nums[i])
                    flag[i] = 1
                    permutation(nums)
                    subset.pop()
                    flag[i] = 0

        permutation(nums)
        return res