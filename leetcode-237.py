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
    def deleteNode(self,head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        n = node
        n.val = n.next.val
        n.next = n.next.next
        
solution = Solution()
linked =Linkedlist()
head = linked.createList([0,0,2,3,4,5])
node = 3
ansNode = solution.deleteNode(head,node)
linked.printList(ansNode)