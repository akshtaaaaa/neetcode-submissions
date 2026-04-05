class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]+=1
            # print(count)
        for val,countval in count.items():
            freq[countval].append(val)
        # print("#####")
        res=[]
        # print("freq: ", freq)
        # print("count: ", count)
        for i in range(len(freq)-1,0,-1):
            # print(i)
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
        