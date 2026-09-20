class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        chars = set()
        if not s:
            return 0
        if len(s) == 1:
            return 1
        chars.add(s[i])
        best = 1
        cur = 1

        while j < len(s):
            r = s[j]
            while r in chars:
                best = max(cur, best)
                cur -= 1
                chars.remove(s[i])
                i += 1
                
            else:
                cur += 1
                chars.add(r)
                j += 1
        best = max(cur, best)
        return best