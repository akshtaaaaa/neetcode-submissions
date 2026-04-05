class Solution:

    def encode(self, strs: List[str]) -> str:
        returnstr=""
        for i in strs:
            length=len(i)
            encoded=str(length)+"#"+i
            returnstr=returnstr+encoded
        return returnstr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # find the separator
            while s[j] != "#":
                j += 1
            # get full length (can be multiple digits!)
            length = int(s[i:j])
            # move past "#"
            j += 1
            
            # extract string
            res.append(s[j:j+length])
            
            # move pointer
            i = j + length
        
        return res
