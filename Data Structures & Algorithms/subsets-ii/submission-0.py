class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        nums.sort()

        def picker(i):
            if i >= (len(nums)):
                res.append(subset[::])
                return

            subset.append(nums[i])
            picker(i+1)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            picker(i+1)

        picker(0)
        return res
        