class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # This is to make sure nums1 is the larger list than nums2
        if len(nums1) < len(nums2):
            L = nums1
            nums1 = nums2
            nums2 = L
        
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2

        if n1 == 0:
            return nums2[n2 // 2] if n2 % 2 == 1 else (nums2[(n2-1)//2] + nums2[n2//2])/2

        if n2 == 0:
            return nums1[n1 // 2] if n1 % 2 == 1 else (nums1[(n1-1)//2] + nums1[n1//2])/2

        if nums1[n1-1] <= nums2[0]:
            if n1 > n2:
                return nums1[(n-1)//2] if n % 2 == 1 else (nums1[(n-1)//2] + nums1[n//2])/2
            else:
                return (nums1[n1-1] + nums2[0])/2

        if nums2[n2-1] <= nums1[0]:
            if n1 > n2:
                return nums1[(n-1)//2 - n2] if n % 2 == 1 else (nums1[(n-1)//2 - n2] + nums1[n//2 - n2])/2
            else:
                return (nums2[n2-1] + nums1[0])/2


        left = 0
        right = n2 - 1

        while left <= right:
            pos_2 = left + (right - left) // 2
            pos_1 = n // 2 - pos_2 - 1
            # since n1 > n2, and we are looping on nums2
            # pos1 will always be will be valid :
            # 0 <= n1/2 - n2/2 <= pos1 <= n1/2 + n2/2 <= n1
            left_max = max(nums1[pos_1], nums2[pos_2])
            # Note than both pos_1 and pos_2 will never reach 0
            # as we are looping so that we get closer to the median
            if pos_2 == n2-1:
                right_min = nums1[pos_1 + 1]
            elif pos_1 == n1-1:
                right_min = nums2[pos_2 + 1]
            else:
                right_min = min(nums1[pos_1 + 1], nums2[pos_2 + 1])
            
            if left_max <= right_min:
                # Found a valid partition
                print(f'Pos 1 = {pos_1}, Pos 2 = {pos_2}, Left Max = {left_max}, Right Min = {right_min}.')
                return left_max if n % 2 == 1 else (nums1[pos_1] + nums2[pos_2]) / 2
            else:
                # This means either nums2[pos_2] > nums1[pos_1 + 1]
                # or nums1[pos_1] < nums2[pos_2 + 1].
                if pos_1 < n1 and nums2[pos_2] > nums1[pos_1 + 1]:
                    right = pos_2 - 1
                else:
                    left = pos_2 + 1

        return None