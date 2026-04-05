class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed={}

        for i in range(len(nums)):
            needed=target - nums[i]
            if needed in traversed.keys():
                return [traversed[needed],i]
            traversed[nums[i]]=i
        return [-1,-1]

        