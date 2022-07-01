# def mergeTwoLists(list1, list2):
#     Mlist = []
#     for i in list1:
#         Mlist += str(i)
#     for i in list2:
#         Mlist += str(i)
#     Mlist.sort()
#     return Mlist

# def mergeTwoLists(list1, list2):
#     for i in list2:
#         list1.append(i)
#     list1.sort()
#     return list1

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
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2: # while list1 and list2 are != 0
            if list1.val < list2.val:
                tail.next =list1
                list1 = list1.next
            else:
                tail.next= list2
                list2= list2.next
            tail = tail.next

        if list1:
            tail.next =list1
        else:
            tail.next =list2
        return dummy.next

# list1 = [1,2,4]
# list2 = [1,3,4]
# l1 = ListNode(list1, None)
# l2 = ListNode(list2, None)
solution = Solution()
linked =Linkedlist()
list1 = linked.createList([1,2,4])
list2 = linked.createList([1,3,4])

ansNode = solution.mergeTwoLists(list1,list2)
linked.printList(ansNode)