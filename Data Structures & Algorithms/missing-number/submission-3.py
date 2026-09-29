class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi=len(nums)
        if maxi not in nums:
            return maxi
        start=0
        for i in nums:
            print(i," ", start)
            if (start not in nums):
                return start
            start+=1

        

            