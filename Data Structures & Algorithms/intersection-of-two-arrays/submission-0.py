class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=set()
        n1=0
        n2=0

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                inter.add(nums1[i])
        print(inter)

        for i in range(len(nums2)):
            if nums2[i] in inter:
                continue
            if nums2[i] in nums1:
                inter.add(nums2[i])
        print(inter)  

        return list(inter) 