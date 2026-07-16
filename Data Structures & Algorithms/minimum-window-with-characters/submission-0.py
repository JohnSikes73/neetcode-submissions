from collections import Counter
from numpy import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(t)
        n = len(s)

        D = Counter(t)

        print(D)

        # This will keep track of the number of characters from t
        # which are present in the current window
        present = 0

        def ADD(c):
            nonlocal present
            if c in D.keys():
                if D[c] > 0:
                    present += 1
                D[c] -= 1    
            return None

        def REMOVE(c):
            nonlocal present
            if c in D.keys():
                if D[c] >= 0:
                    present -= 1
                D[c] += 1
            return None

        left = 0
        right = 0
        min_window = [0, inf]

        ADD(s[right])
        while left < n: 
            if present == m:
                if right - left < min_window[1] - min_window[0]:
                    min_window = [left, right]
                REMOVE(s[left])
                left += 1
            elif right < n-1:
                right += 1
                ADD(s[right])
            else:
                REMOVE(s[left])
                left += 1

        if min_window[1] == inf:
            return ''
        
        return s[min_window[0]:(min_window[1]+1)]