class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = 0
        r = n-1
        min_elt = float('inf')
        while l <= r:
            
            if r - l == 1:
                return min(min_elt, nums[l], nums[r])

            m = l + (r-l)//2
            #print(f'Left = {l}, Mid = {m}, Right = {r}')
            
            if nums[l] < nums[m]:
                if nums[m] < nums[r]:
                    return min(min_elt, nums[l])
                else:
                    l = m + 1
            else:
                # this means left is greater than the mid
                # so the min has to be in between them
                min_elt = min(min_elt, nums[m])
                r = m - 1
        
        return min_elt