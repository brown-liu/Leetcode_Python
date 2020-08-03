# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    def mergeTwoLists(self, l1, l2):

        if l1==None and l2!=None: return l2
        if l2==None and l1!=None: return l1

        if l1.val< l2.val:
            head, prev, l1= l1,l1,l1.next

        else:
            head, prev, l2 = l2, l2, l2.next


        while l1 != None and l2 != None:
            if l1.val < b.val:
                prev.next = a
                prev, a = a, a.next
            else:
                prev.next = b
                prev, b = b, b.next
        if a != None: prev.next = a
        if b != None: prev.next = b
        return head
'''

'''
class Solution:

    def __init__(self):
        self.head = self.ref = None

    def mergeTwoLists(self, l1, l2):
        while l1 and l2:
            if l1.val < l2.val:
                next = l1
                l1 = l1.next
            else:
                next = l2
                l2 = l2.next
            self.append(next)
        if l1:
            self.append(l1)
        elif l2:
            self.append(l2)
        return self.head

    def append(self, node):
        if not self.head:
            self.head = self.ref = node
        else:
            self.ref.next = node
            self.ref = self.ref.next
            
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        t = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next
        t.next = l1 or l2
        return head.next
