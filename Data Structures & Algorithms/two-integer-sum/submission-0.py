class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i , j = 0 , len(nums)-1
        ans = []

        while i <= j:
            if nums[i] + nums[j] == target:
                ans.extend([i, j])
                break
            elif nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
        return ans