# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr,prev= head,None
        while curr:
            temp= curr.next
            curr.next= prev
            prev= curr
            curr=temp
        count=1
        dummy= ListNode(0,prev)
        new,old= None,prev

        while old:
            
            if(count==n):
                if(old.next==None):
                    return new
                else:
                    old=old.next
            temp=old.next
            old.next= new 
            new=old
            old=temp
            count=count+1
        
        
        return new

        
            
            




        