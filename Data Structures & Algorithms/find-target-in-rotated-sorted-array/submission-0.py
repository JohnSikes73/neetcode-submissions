class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n-1

        while l <= r:

            m = l + (r-l)//2
            #print(f'Left = {l}, Mid = {m}, Right = {r}')
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                # left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1