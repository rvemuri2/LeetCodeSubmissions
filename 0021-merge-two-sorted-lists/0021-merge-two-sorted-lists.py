# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
       
        
        curr = ListNode()
        tail = curr
        
        if(list1 == None and list2 == None):
            return list1
        
        else:
            while(list1 and list2):
                
                if(list1.val < list2.val):
                    tail.next = list1
                    list1 = list1.next
                    
                elif(list1.val > list2.val):
                    tail.next = list2
                    list2 = list2.next
                    
                elif(list1.val == list2.val):
                    tail.next = list2
                    list2 = list2.next
                    
                    
                tail = tail.next
                
            if(list1 != None):
                tail.next = list1
            elif(list2 != None):
                tail.next = list2
                
                    
            return curr.next
                
             
            
        
        