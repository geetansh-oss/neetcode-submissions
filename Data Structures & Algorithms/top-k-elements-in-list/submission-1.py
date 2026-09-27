class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        map = {}
        count = [[] for _ in range(len(nums)+1)]

        for num in nums:
            map[num] = map.get(num, 0) + 1

        for key, value in map.items():
            count[value].append(key)

        for lst in reversed(count):
            for num in lst:
                if len(ans) < 2:
                    ans.append(num)

        return ans