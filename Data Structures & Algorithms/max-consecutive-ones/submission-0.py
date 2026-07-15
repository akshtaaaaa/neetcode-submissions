class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons=0
        counter=0
        for i in nums:
            if i == 1:
                counter +=1
            elif i ==0:
                max_cons = max(max_cons, counter)
                counter =0
        max_cons = max(max_cons, counter)
        return max_cons
        