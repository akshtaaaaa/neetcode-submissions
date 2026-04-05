class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets=set()
        for i in range(n):
            setNums=set()
            for j in range(i+1, n):
                valToCheck=-(nums[i]+nums[j])
                if valToCheck in setNums:
                    triplets.add(tuple(sorted([nums[i],nums[j], valToCheck])))
                else:
                    setNums.add(nums[j])
        return list(triplets)

        