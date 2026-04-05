import heapq
import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]
        for i in range(len(lists)):
            # print(i)
            # print(lists[i].val)
            # print(lists[i])
            heapq.heappush(pq, (lists[i].val,i, lists[i]))
        
        dummy=ListNode(None)
        temp=dummy
        while pq!=[]:
            minval,idx,node=heapq.heappop(pq)
            temp.next=node
            if node.next:
                heapq.heappush(pq, (node.next.val,idx, node.next))
            temp=temp.next

        return dummy.next




        