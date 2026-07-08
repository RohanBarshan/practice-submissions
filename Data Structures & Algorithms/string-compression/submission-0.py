class Solution:
    def compress(self, chars: List[str]) -> int: 
        n = len(chars)
        k = 0
        i = 0
        
        while i < n:
            char = chars[i]
            chars[k] = char
            k += 1
            j = i + 1

            while j < n and chars[j] == char:
                j += 1

            if j - i > 1:
                for c in str(j - i):
                    chars[k] = c
                    k += 1
            
            i = j
        return k