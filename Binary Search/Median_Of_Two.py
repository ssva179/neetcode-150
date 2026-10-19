class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newLst = nums1+nums2
        newLst.sort()
        if len(newLst)%2==0:
            l = newLst[len(newLst)//2-1]
            r = newLst[len(newLst)//2]
            return (l+r)/2.0
        else:
            return newLst[len(newLst)//2]
