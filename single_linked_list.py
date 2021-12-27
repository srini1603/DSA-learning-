class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList :
    def __init__(self):
        # new_node=Node(value)
        self.head = None
        self.tail = None
        self.length = 0

    def Append (self,value):
        new_node=Node(value)
        # append element in last of the list
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            # self.tail.next = new_node
            # node_node = self.tail
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            self.tail = new_node
        self.length +=1

    def Pop(self):
        # can be done using pre and temp
        # in while loop pre is current temp and temp is temp.next
        # if temp.next is null tail is pointed towards pre and tail.next is None
        # temp is returned to clear the memory
        # (dis: incase we forgot to return temp may stored there for ever still the operatiom is done)
        # this method used when we are required to return the poped value
        if self.head is None:
            print("can't pop an empty list")
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.length -= 1

    def Prepend(self,value):
        # add element to the starting of the element
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head=new_node
        self.length +=1


    def Prepop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            temp=self.head
            self.head = None
            self.tail = None
            self.length -=1
            return temp
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def Get(self,index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def Set(self,index,value):
        temp=self.Get(index)
        if temp is not  None:
            temp.value =value
            return True
        return False

    def Insert(self,index,value):
        new_node = Node(value)
        if index > self.length or index < 0:
            return None
        if index == self.length and index > 0: # and index > 0 becoze if the list is empty length is 0
            self.tail.next = new_node # or need to travser till the temp meet None
            new_node = self.tail
            self.length += 1
        if index == 0:
            temp = self.head
            new_node.next = temp
            self.head = new_node
            self.length += 1
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True #optional may need in somecase


    def Remove(self,index):
        temp = self.head
        prev = self.head
        if index > self.length or index < 0:
            return None
        elif index == 0:
            if temp.next == None:
                self.head = None
                self.tail = None
                self.length -= 1
                return True
            else:
                self.head = temp.next
                temp.next = None

            self.length -= 1

        elif index == (self.length -1 ) and index > 0:
            return self.Pop()

        else:
            for _ in range(index-1):
                temp = temp.next
                prev = temp
            temp = temp.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1

    def RemoveByValue(self,value):
        temp =self.head
        prev = self.head
        while temp is not None:
            if temp.value == value:
                if temp == self.head:
                    self.head = temp.next
                    self.length -= 1
                    return True
                if temp.next == None:
                    prev.next = None
                    self.tail = prev
                    self.length -= 1
                    return True
                prev.next = temp.next
                temp.next = None
                self.length -= 1
                return True
            prev = temp
            temp = temp.next


    def Reverse(self):
        self.tail =self.head
        before = None
        temp = self.head
        if self.head is None:
            return self.head        ##         self.head
        while temp is not None:       #         |
            after = temp.next       #  none(<-) a  -> b -> c -> d -> none
            temp.next = before      #  |        |       |
            before = temp           #  before  temp   after(temp.next)
            temp = after

        self.head = before




    def PrintList(self):
        # print the linked_list
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        print("length of list is " + str(self.length))


mynode = LinkedList()
# mynode.Prepop()
# mynode.Prepend(1)
mynode.Insert(0,0)
mynode.Append(4)
mynode.Append(6)
mynode.Append(9)
# mynode.PrintList()
# mynode.Pop()
# mynode.PrintList()
mynode.Append(5)
# mynode.Prepop()
# mynode.PrintList()
mynode.Set(1,8)
mynode.Prepend(2)
mynode.Insert(3,0)
mynode.PrintList()
mynode.RemoveByValue(2)
mynode.RemoveByValue(0)
mynode.Remove(3)
#mynode.Reverse()
mynode.PrintList()
