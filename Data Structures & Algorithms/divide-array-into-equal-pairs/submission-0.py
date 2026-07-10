class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        length=len(nums)
        if length%2==0:
            arrs={}
            for i in nums:
                if i in arrs.keys():
                    arrs[i]+=1
                else:
                    arrs[i]=1
            for k,v in arrs.items():
                if v%2!=0:
                    return False
            return True
        else:
            return False
        