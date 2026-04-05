class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total=1
        left=0
        right=1
        if len(s) == 0:
            return 0
        travelled=s[left]
        maxtotal=total
        while right < len(s):
            if s[right] in travelled:
                left+=1
                right=left+1
                travelled=s[left]
                total=len(travelled)
            else:
                travelled+=s[right]
                total+=1
                right+=1
            maxtotal=max(maxtotal,total)
            
            # print(travelled)
        return maxtotal
        