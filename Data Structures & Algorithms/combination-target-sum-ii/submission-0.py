class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def picker(i, sum):
            if sum == target:
                res.append(subset[::])
                return

            if sum > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            picker(i+1, sum + candidates[i])
            subset.pop()

            while (i + 1 < len(candidates) and candidates[i] == candidates[i + 1]):
                i += 1
            picker(i+1, sum)

        picker(0, 0)

        return res     