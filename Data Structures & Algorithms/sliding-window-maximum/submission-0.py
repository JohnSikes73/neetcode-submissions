from collections import deque
from numpy import inf

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        D = deque([[-inf, -inf]])

        for i in range(k):
            x = nums[i]
            while D and x > D[-1][0]:
                D.pop()
            D.append([x,i])

        n = len(nums)
        result = []
        for i in range(k,n):
            result.append(D[0][0])
            if D[0][1] <= i - k:
                D.popleft()
            x = nums[i]
            while D and x > D[-1][0]:
                D.pop()
            D.append([x,i])

        result.append(D[0][0])

        return result