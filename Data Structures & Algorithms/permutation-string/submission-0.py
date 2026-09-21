class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = [0] * 26
        for ch in s1:
            idx = ord(ch) - ord("a") 
            counts[idx] += 1
        
        i = 0
        j = 0
        cur = [0] * 26
        for _ in range(len(s1)):
            chh = s2[j]
            idxx = ord(chh) - ord("a") 
            cur[idxx] += 1
            j += 1
        
        if cur == counts:
            return True
        
        while j < len(s2):
            cur[ord(s2[j]) - ord("a")] += 1
            cur[ord(s2[i]) - ord("a")] -= 1
            
            i += 1
            j += 1
            
            if cur == counts:
                return True
            
        return False



    
    
        

        


