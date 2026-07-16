class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if h == n:
            return max(piles)

        def compute_hours(k):
            s = 0
            for pile in piles:
                # calculating ceiling of pile / k
                s += -(pile // -k)
            return s

        left_k = 1
        right_k = max(piles)
        min_k = right_k

        while left_k <= right_k:
            mid_k = left_k + (right_k - left_k) // 2
            hours = compute_hours(mid_k)
            if hours == h:
                # If k-1 yields higher hours, then k is the minimal k which
                # yields h hours. Else, take right = k-1 and continue.
                if mid_k == 1:
                    return 1
                else:
                    min_k = min(mid_k, min_k)
                    right_k = mid_k - 1
            elif hours < h:
                # If k = mid_k, then the bananas will be finished before h hours
                # so the rate needs to be slowed. So k needs to be reduced.
                right_k = mid_k - 1
            else:
                left_k = mid_k + 1

        return min(left_k, min_k)