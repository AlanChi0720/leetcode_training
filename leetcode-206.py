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

class Solution: # iteratively: time O(n) space O(1)
    def reverseList(self, head):
        if not head:
            return None
        ans, p1, p2 = head, head, head
        ans = ans.next
        p1 = ans
        p2.next = None
        while ans:
            ans = ans.next
            p1.next = p2
            p2 = p1
            p1 = ans
        return p2
        
class Solution: # recursively: time O(n) space O(n)
    def reverseList(self, head):  
        if not head:
            return None
        ans = head
        if head.next:
            ans = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return ans
    
solution = Solution()
linked =Linkedlist()
head = linked.createList([1,2,3])
ansNode = solution.reverseList(head)
linked.printList(ansNode)