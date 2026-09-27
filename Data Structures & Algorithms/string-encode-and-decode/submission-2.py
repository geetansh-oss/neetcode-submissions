class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res = res + str(len(st)) + "#" + st

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#" and j < len(s):
                j += 1

            size = int(s[i : j])    
            res.append(s[j+1: j+1+size])
            i = j + 1 + size

        return res
