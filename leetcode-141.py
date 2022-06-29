from math import trunc


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

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head 
        while fast !=  None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

solution = Solution()
linked =Linkedlist()
head = linked.createList([3,2,0,-4])
ansNode = solution.hasCycle(head)
linked.printList(ansNode)