class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        l1 = n1 - n2
        l2 = n2 -n1
        l3 = []
        l3.append(list(l1))
        l3.append(list(l2))
        return l3
        