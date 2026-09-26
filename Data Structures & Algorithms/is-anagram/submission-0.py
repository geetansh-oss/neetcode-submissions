class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        freq = {}
        for chr in s:
            freq[chr] = freq.get(chr, 0) + 1
        
        for chr in t:
            freq[chr] = freq.get(chr, 0) - 1
            if(freq[chr] <= 0):
                freq.pop(chr)

        if(len(freq) == 0): 
            return True

        return False