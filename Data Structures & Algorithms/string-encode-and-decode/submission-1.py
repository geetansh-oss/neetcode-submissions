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
            if s[i].isdigit() and s[i+1] == "#":
                sub_str = int(s[i])
                res.append(s[i+2: i+2+sub_str])
                i = i+2+sub_str

        return res
