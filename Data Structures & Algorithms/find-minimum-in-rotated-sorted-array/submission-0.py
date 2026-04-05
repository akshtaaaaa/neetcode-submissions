class Solution:
    def findMin(self, nums: List[int]) -> int:
        r_ele=nums[-1]
        for i in nums:
            if i>r_ele:
                continue

            return i