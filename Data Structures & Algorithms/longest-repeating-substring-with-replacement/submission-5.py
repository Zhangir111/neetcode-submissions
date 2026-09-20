class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        counts = {}
        best = 1

        for r in range(len(s)):
            ch = s[r]
            counts[ch] = counts.get(ch, 0) + 1
            max_freq = max(counts[ch], max_freq)
        
            while (r - l + 1) > max_freq + k:
                counts[s[l]] -= 1
                l += 1
            
            best = max((r-l+1), best)
        
        return best
    

