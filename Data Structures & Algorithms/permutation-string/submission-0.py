class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1:
            return False

        # This is to maintain the count of the s1 elements
        D = defaultdict(int)
        for i in range(n1):
            c = s1[i]
            D[c] += 1

        # This is to maintain the elements of s1 whose freq does not match in the current window
        Z = set(D.keys())

        def ADD(c):
            if c in D.keys():
                D[c] -= 1
                if D[c] == 0:
                    Z.discard(c)
                else:
                    Z.add(c)
            return None

        def REMOVE(c):
            if c in D.keys():
                D[c] += 1
                if D[c] == 0:
                    Z.discard(c)
                else:
                    Z.add(c)
            return None


        for i in range(n1):
            c = s2[i]
            ADD(c)
        
        if not Z:
            return True
        else:
            if n2 == n1:
                return False

        
        for right in range(n1,n2):
            r = s2[right]
            l = s2[right-n1]
            ADD(r)
            REMOVE(l)
            if not Z:
                return True
        
        return False