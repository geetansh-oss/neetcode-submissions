class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i , j = 0 , len(nums)-1
        freq = {}
        for i in range(0, len(nums)):
            freq[nums[i]] = i
        
        print(freq)
        ans = []

        for i in range(0, len(nums)):
            temp = target - nums[i]
            if temp in freq:
                ans.append(i)
                ans.append(freq.get(temp))
                break

        ans.sort()
        return ans