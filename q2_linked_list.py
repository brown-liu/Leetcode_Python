# List Node
'''
Reference: stackabuse.com/python-linked-lists/
A single list element is called a node.
End of the list will be a NIL element (None in python).
Single linked => A node point to the next element(Next Node)
Double linked => node point to the next and previous node.
List Node is not a pre-set data type in python = > have to make one up when needed
'''

###################_____this is an example of ListNode _______-######################################
class ListNode():
    # __init__ as constructor
    def __init__(self,value):
        self.value=value
        # 'next' works like a C pointer to assign the address for next node
        self.next=None

    def has_value(self,value):
        #check if init is done.
        if self.value==value:
            return True
        else:
            return False

class Single_Linked_list():
    def __init__(self):
        self.head=None
        self.tail=None
        return

    def Add_list(self,item):
        if not isinstance(item,ListNode):
            item=ListNode(item)

        if self.head == None:
            self.head=item
        else:
            self.tail.next=item
        self.tail=item
        return


    def List_length(self):
        count=0
        current_node=self.head
        while current_node!= None:
            count+=1
            current_node=current_node.next
        return count

    def Print_list(self):
        current_node=self.head
        while current_node!=None:
            print(current_node.value)
            current_node=current_node.next
        return

    def Search(self,value):
        current_node=self.head
        index=-1
        while current_node!=None:
            index+=1
            if current_node.value==value:
                print(f"found{value} in {index}th Node")
                current_node = current_node.next

            else:
                current_node = current_node.next

        return


############################answer to question 2###################################
'''class Solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode) -> ListNode:
        ans=ListNode(0)
        temp=ans
        tempsum=0
        while True:
            if l1!=None:
                tempsum+=l1.val
                l1=l1.next
            if l2!=None:
                tempsum+=l2.val
                l2=l2.next
            temp.val=tempsum % 10
            tempsum //=10
            if l1==None and l2==None and tempsum==0:
                break
            temp.next=ListNode(0)
            temp=temp.next
        return ans

'''














