# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import heapq
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val,i, lists[i]))
        
        head = dummy = ListNode(None)
        while heap:
            val, index, node = heapq.heappop(heap)
            dummy.next = node
            dummy = dummy.next
            if node.next:
                heapq.heappush(heap, (node.next.val,index, node.next))
        
        return head.next
