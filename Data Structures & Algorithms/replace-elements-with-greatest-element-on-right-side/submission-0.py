class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newl=[None]*len(arr)
        for i in range(len(arr)):
            if i == (len(arr)-1):
                newl[i]=-1
                break
            else:
                newl[i]=max(arr[i+1:])
        return newl
        