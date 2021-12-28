class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def Append(self,value):
        new_node = Node(value)
        temp = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        while temp.next is not None: # new_node.previous = self.tail
            temp = temp.next         # self.tail = new_node
        temp.next = new_node        # new_node.next = None
        new_node.next = None
        new_node.previous = temp
        self.tail = new_node
        self.length += 1

    def Prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        self.length += 1

    def PrePop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        else:
            temp1 = self.head
            temp2 = temp1.next
            temp1.next = None
            temp2.previous = None
            self.head = temp2
            self.length -= 1
            return True

    def Get(self,index):
        temp1 =self.head
        temp2 = self.tail
        if index < 0 or index > self.length-1: # length start with 1
            return None
        elif index <= self.length//2:
            for _ in range(index):
                temp1 = temp1.next
            return temp1 # temp.value
        else:
            for _ in range(self.length-1,index,-1):
                temp2 = temp2.previous
            return temp2 # temp.value

    def Setvalue(self,index,value):
        temp = self.Get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def Insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.length += 1
            return True

        else:
            temp = self.head
            for _ in range (index):
                temp = temp.next
            if temp is None:
                return self.Append(value)
            new_node.next = temp
            new_node.previous = temp.previous
            temp.previous.next = new_node
            temp.previous = new_node
            self.length += 1

    def Pop(self):
        temp = self.head
        if temp is None:
            return None
        elif temp.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            while temp.next.next is not None:
                temp = temp.next
            temp.next.previous = None
            temp.next = None
            self.length -= 1


    def Remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.PrePop()
        elif index == self.length -1:
            return self.Pop()
        else:
            temp = self.Get(index)
            prev = temp.previous
            after = temp.next
            after.previous =  prev
            prev.next = after
            self.length -= 1
            return temp

    def RemoveByValue(self,value):
        temp = self.head
        while temp.value is not value:
            temp = temp.next
            if temp is None:
                return False
        before = temp.previous
        after = temp.next
        before.next = after
        after.previous = before
        self.length -= 1
        return temp
    def PrintList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("len of list is "+str(self.length))

mynode = DoublyLinkedList(2)
mynode.Prepend(0)
mynode.Prepend(1)
mynode.Append(3)
mynode.Setvalue(2,10)
#mynode.PrePop()
mynode.Append(4)
mynode.Insert(0,9)
mynode.RemoveByValue(3)
mynode.PrintList()
#print("dd"+str(mynode.Get(4)))

