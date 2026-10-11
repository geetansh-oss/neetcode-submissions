class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        sub_arr = []

        def dfs(i):
            if i >= len(nums):
                res.append(sub_arr.copy())
                return 

            sub_arr.append(nums[i])
            dfs(i+1)
            sub_arr.pop()
            dfs(i+1)

        dfs(0)
        return res