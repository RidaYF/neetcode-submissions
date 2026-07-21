class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        st = sorted(t)

        if ss == st:
            return True
        else:
            return False