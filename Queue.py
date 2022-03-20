class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
# adding in last is O(1) since we known the tail or last
# removing in start is O(1) since it is the head or First
# FIFO
class queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last  = new_node
        self.length = 1

    def Enqueue(self,value):    # append in last
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return True
        temp = self.last        # can be even by travering
        temp.next = new_node
        self.last = new_node

    def Dequeue(self):
        temp = self.first
        if self.first is None:
            return None
        elif temp.next is None:
            self.first = None
            self.last  = None
            self.length -= 1
            return True, temp
        else:
            self.first = temp.next
            temp.next = None
            self.length -= 1
            return  True ,temp



    def PrintQueue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

my_queue = queue(3)
my_queue.Enqueue(2)
my_queue.Enqueue(5)
my_queue.PrintQueue()
print("\nafter dequeue\n")
my_queue.Dequeue()
# my_queue.Enqueue(4)
# my_queue.Enqueue(33)
my_queue.PrintQueue()
# my_queue.Dequeue()
# print()
# my_queue.PrintQueue()
print("I am changing")