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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        pointA = headA
        pointB = headB
        check = set()
        while pointA:
            check.add(pointA) # store the nodes which have been visited
            # print(check)
            pointA = pointA.next
        while pointB:
            if pointB in check:
                return pointB
            pointB = pointB.next
        return None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode):
#         pointA, pointB = headA, headB
#         while pointA != pointB:
#             pointA = pointA.next if pointA else headB
#             pointB = pointB.next if pointB else headA
#         return pointA
        # while pointA != pointB:
        #     if pointA:  # pointA == True
        #         pointA = pointA.next
        #     else:
        #         pointA = headB
        #     if pointB: # pointB == True
        #         pointB = pointB.next
        #     else:
        #         pointB = headA
        # return pointA

solution = Solution()
linked =Linkedlist()
list1 = linked.createList([4,1,8,4,5])
list2 = linked.createList([5,6,1,8,4,5])
ansNode = solution.getIntersectionNode(list1,list2)
linked.printList(ansNode)