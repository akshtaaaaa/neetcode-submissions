class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        for i in range(n+1):
            print("i:",i)
            count=0
            while i!=0:
                # print("n:"n)
                i= i & (i-1)
                count+=1
            print(count)
            output.append(count)
        return output
        