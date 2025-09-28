import heapq
class linked_list(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    # resverse a linked list
    def reverse(self, head):
        prev=None
        current=head

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev
    
    # linked list cycle
    def hasCycle(self,head):
        if head is None or head.next is None:
            return False
        
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
        return False
    
    # Merge two sorted 
    def mergesorted(self, L1,L2):
        dummy=linked_list(val=-1)
        curr=dummy

        while L1 and L2:
            if L1.value < L2.value:
                curr.next=L1
                curr=L1
                L1=L1.next
            else:
                curr.next=L2
                curr=L2
                L2=L2.next
        curr.next=L1 if L1 else L2
        return dummy.next
    
    # Remove Nth node from end of list
    def removeNthFromEnd(self, head, n):
        dummy=linked_list(0)
        dummy.next=head
        first=dummy
        second=dummy

        for _ in range(n+1):
            second=second.next
        
        while second:
            first=first.next
            second=second.next
        
        first.next=first.next.next
        return dummy.next
    
    # reorder List
    def reorderList(self, head):
        if not head:
            return
        
        # find the middle of the linked list
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # reverse the second half of the linked list
        prev=None
        curr=slow
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        
        # merge the two halves
        first,second=head,prev
        while second.next:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first,temp1=first.next,temp1
            second,temp2=second.next,temp2
        return head
    
    # plus one linked list
    def plusOne(self, head):
        dummy=linked_list(0)
        dummy.next=head
        not_nine=dummy

        # find the rightmost not nine
        curr=head
        while curr:
            if curr.value != 9:
                not_nine=curr
            curr=curr.next
        
        # increase this rightmost not nine by 1
        not_nine.value += 1
        not_nine=not_nine.next

        # set all the following nines to zeros
        while not_nine:
            not_nine.value=0
            not_nine=not_nine.next
        
        if dummy.value == 1:
            return dummy
        return head
    
    #middle of the linked list
    def middleNode(self,head):
        slow , fast=head, head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    
    #remove duplicates from sorted list
    def deleteDuplicates(self, head):
        curr=head

        while curr and curr.next:
            if curr.value == curr.next.value:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
    
    