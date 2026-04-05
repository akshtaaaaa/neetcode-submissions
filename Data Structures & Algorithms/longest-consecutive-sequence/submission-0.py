class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen=0
        total=1
        setNums= set(nums)
        for i in setNums:
            val_to_check=i+1
            while val_to_check in setNums:
                total+=1
                val_to_check+=1
            maxlen=max(total,maxlen)
            total=1
        return maxlen
        