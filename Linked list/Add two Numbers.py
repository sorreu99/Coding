# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head=None
    def addTwoNumbers(self, l1, l2):
            output=ListNode(0)
            dummy=output
            carry=0
            while l1 or l2 or carry :

                val1=l1.val if l1 else 0
                val2=l2.val if l2 else 0
                agg=(val1+val2+carry)%10
                print('agg is',agg)
                carry=(val1+val2+carry)//10
                print('carry is',carry)
                
                dummy.next=ListNode(agg)
                dummy=dummy.next
                print("dmmy cureent val",dummy.val)
                
                l1=l1.next if l1 else None
                l2=l2.next if l2 else None
            return output.next

    def push(self,val):
        newnode=ListNode(val)
        newnode.next=self.head
        self.head=newnode
    def printlist(self,head1):
        temp=head1
        while temp:
            print(temp.val,end=" ")
            temp=temp.next
        print()


l1=LinkedList()
l1.push(9)
l1.push(9)
l1.push(9)
l1.push(9)
l1.printlist(l1.head)
l2=LinkedList()
l2.push(9)
l2.push(9)
l2.printlist(l2.head)
l3=LinkedList()

l3.head=l3.addTwoNumbers(l1.head,l2.head)
l3.printlist(l3.head)


            