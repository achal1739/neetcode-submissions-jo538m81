class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            A, B = B, A
        
        left = 0
        right = len(A) - 1
        while True:
            mid_a = (left+right)//2
            mid_b = half - mid_a - 2

            Aleft = A[mid_a] if mid_a >= 0 else float("-inf")
            Aright = A[mid_a+1] if (mid_a+1) < len(A) else float("inf")
            Bleft = B[mid_b] if mid_b >= 0 else float("-inf")
            Bright = B[mid_b+1] if (mid_b+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                right = mid_a - 1
            else:
                left = mid_a + 1



