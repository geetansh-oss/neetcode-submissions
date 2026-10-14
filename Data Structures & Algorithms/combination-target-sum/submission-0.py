class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def picker (i, nums, target, sum):
            if i >= len(nums) or sum > target:
                return

            if sum == target: 
                res.append(subset[::])
                return

            subset.append(nums[i])
            picker(i, nums, target, sum + nums[i])
            subset.pop()

            picker(i+1, nums, target, sum)

        picker(0, nums, target, 0)
        return res