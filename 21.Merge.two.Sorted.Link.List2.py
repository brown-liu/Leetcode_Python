class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoListsSolution1(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:  # 1
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:  # 2
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


    # def mergeTwoListsSolution2(self, l1, l2):
        # List_result = ListNode()
        # if l1.val > l2.val:
        #     List_result.val = l2
        #     l2=l2.next
        #
        # elif l1.val < l2.val:
        #     List_result.val = l1
        #     l1=l1.next
        # List_result.next = l2.val
        # return List_result


    def mergeTwoListsSolution3(self, l1, l2):
        if l1==None:return l2
        if l2==None:return l1

        if l1.val<l2.val:
            head, prev, l1= l1, l1, l1.next

        else:
            head, prev, l2= l2, l2, l2.next

        while l1!=None and l2!=None:
            if l1.val<l2.val:
                prev.next=l1
                prev, l1= l1, l1.next
            else:
                prev.next=l2
                prev, l2= l2, l2.next
        if l1 != None:
            prev.next=l1
        if l2 != None:
            prev.next=l2
        return head

a=ListNode(10)
b=ListNode(20)
solution=Solution1()
x=solution.mergeTwoListsSolution3(a,b)
print(x.next.val)