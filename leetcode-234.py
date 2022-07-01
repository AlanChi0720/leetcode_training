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
    def isPalindrome(self, head):
        checklist= ""
        while head:
            checklist += str(head.val)
            head = head.next
        # check palidrome
        # print(checklist)
        if str(checklist)== str(checklist)[::-1]:
            return True
        else:
            return False
class Solution:
    def isPalindrome(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        l,r = 0, len(nums)-1
        while l <= r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            else: # if nums[l] != nums[r]:
                return False
        return True

class Solution: # space: O(1)
    def isPalindrome(self, head):
        fast, slow = head, head
        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # check palindrome
        left, right = head, prev
        while right:
            if left. val != right.val:
                return False
            left = left.next
            right = right.next
        return True

solution = Solution()
linked =Linkedlist()
head = linked.createList([0,0,2,3,4,5])
ansNode = solution.isPalindrome(head)
linked.printList(ansNode)