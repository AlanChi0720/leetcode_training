class ListNode: # bulit a listnode type
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linkedlist(): # bulit a linkedlistt object
    def createList(self, list):
        head = ListNode()
        ptr = head
        for i in list:
            tmp = ListNode(i)
            ptr.next = tmp
            ptr = ptr.next
        return head.next

    def printList(self, node):
        # Linked List traversal
        while node:
            print(node.val)
            node = node.next

# class Solution:
#     def removeElements(self, head, val):
#         dummy = ListNode(next=head)
#         tail = dummy
#         while head:
#             if head.val == val:
#                 tail.next = head.next
#                 head = tail.next
#             else:
#                 tail = head
#                 head = head.next      
#         return dummy.next

class Solution:
    def removeElements(self, head, val):
        curr=ListNode()
        x=curr
        while head: # only for the last 6
            if head.val== val and head.next is None:
                print('if')
                curr.next=head.next
                curr=curr.next
                head=head.next
                break
            if head.val==val:
                print('if2')
                head=head.next
            else:
                print('else')
                curr.next=head
                curr=curr.next
                head=head.next
                continue
        return x.next

solution = Solution()
linked =Linkedlist()
head = linked.createList([1,2,6,3,4,5,6])
val = 6
# head = linked.createList([7,7,7,7])
# val = 7
# head = linked.createList([1])
# val = 2
ansNode = solution.removeElements(head,val)
linked.printList(ansNode)