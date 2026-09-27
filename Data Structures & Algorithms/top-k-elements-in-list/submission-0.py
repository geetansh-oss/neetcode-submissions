class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1

        for key, value in map.items():
            if value >= k:
                ans.append(key)

        return ans