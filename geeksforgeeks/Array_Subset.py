from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        freq_a = Counter(a)
        freq_b = Counter(b)
        
        count = 0
        for key in freq_b:
            if key in freq_a and freq_a[key] >= freq_b[key]:
                count += 1
                
        return count == len(freq_b)
    
    
    
    
