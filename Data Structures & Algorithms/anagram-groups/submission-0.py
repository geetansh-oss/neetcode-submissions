class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = {}

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord("a")] += 1

            key = tuple(count)
            map[key] = map.get(key, [])
            map[key].append(s)

        return list(map.values())  
              