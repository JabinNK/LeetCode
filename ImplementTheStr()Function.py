class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0
        pn = 0
        while pn < n - L + 1:
            while pn < n - L + 1 and needle[0] != haystack[pn]:
                pn += 1
            pl = current_len = 0
            while pl < L and pn < n and needle[pl] == haystack[pn]:
                pn += 1
                pl += 1
                current_len += 1
            if pl == L:
                return pn - L
            pn = pn - current_len + 1 
        return -1