# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def removeN(self, head1, n):
        L=ListNode(0)
        L.next=head1
        R=head1
        head1=L
        
        while n>0:
            R=R.next
            n-=1
        while R:
            L=L.next
            R=R.next
        L.next=L.next.next
        return head1.next

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
l1.head=l1.removeN(l1.head,1)
l1.printlist(l1.head)