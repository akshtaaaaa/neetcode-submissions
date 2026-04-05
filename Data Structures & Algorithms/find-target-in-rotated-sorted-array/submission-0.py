class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        
        while low <= high:
            # find sorted half
            
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            
            if (nums[low]<=nums[mid]): 
                if (target < nums[mid]) and nums[low]<=target:
                    high=mid-1
                else:
                    low=mid+1
                

            elif (nums[mid]<nums[high]): 
                if (nums[mid] < target) and target <= nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            
        return -1  