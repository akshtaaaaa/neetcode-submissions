class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if set(s)!=set(t):
            return False
        sd={}
        td={}
        for i in s:
            if i in sd.keys():
                sd[i]+=1
            else:
                sd[i]=1
        for i in t:
            if i in td.keys():
                td[i]+=1
            else:
                td[i]=1
            
        
        return (sd==td)

        