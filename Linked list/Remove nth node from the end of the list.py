# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def removeN(self, head1, n):
        temp = head1
        lentemp=head1
        temp1 = None
        count = 0
        length=0
        while lentemp:
            length+=1
            lentemp=lentemp.next

        if (length-n)==0:
            
            head1=temp.next

            temp.next=None

            return head1
        
        
        while count <=(length-n):
            
            
            temp1=temp.next
            count+=1

            if count==(length-n):
                
                temp.next=temp1.next
                temp1.next=None
                temp=None
                
                break
            temp=temp.next
        return head1
        

    def push(self, val):
        newnode = ListNode(val)
        newnode.next = self.head
        self.head = newnode

    def printlist(self, head1):
        temp = head1
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


l1 = LinkedList()
l1.push(4)
l1.push(3)
l1.push(2)
l1.push(1)
l1.printlist(l1.head)
l1.head=l1.removeN(l1.head,4)
l1.printlist(l1.head)