class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        best = ""
        best_score = float('inf') #want smallest
        
        #Expand then shrink. Move r+=1 until t in s, then l+=1 keeping t in s. Repeat

        l = 0
        r = 0
        
        need = [0]*200
        for ch in t:
            need[ord(ch)] += 1
        
        required = sum(1 for val in need if val > 0) #unique chars
        window = [0] * 200
        have = 0

        for r in range(len(s)):
            #new char: add to window
            ch = s[r]
            idx = ord(ch)
            window[idx] += 1

            #if it fulfills one requirement: have +=1
            if need[idx] == window[idx]:
                have += 1
            
            #if the window is large enough now
            while have >= required:
                if r - l + 1 < best_score: #check if it's the new best
                    best_score = r - l + 1
                    best = s[l : r + 1]
                window[ord(s[l])] -= 1
                if window[ord(s[l])] == need[ord(s[l])] -1:
                    have -= 1
                l += 1
                    
        
        return best
                



            
            


        
        