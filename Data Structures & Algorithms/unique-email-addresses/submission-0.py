class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique=set()
        for i in emails:
            localname=i.split("@")[0]
            localname=localname.replace(".","")
            domain=i.split("@")[1]
            plus= localname.find("+")
            if plus != -1:
                localname=localname.replace(localname[plus:], "")
            finalemail=localname+"@"+domain
            print(finalemail)
            unique.add(finalemail)
        return len(unique)

            