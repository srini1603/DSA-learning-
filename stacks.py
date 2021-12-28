class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node =Node(value)
        self.top = new_node
        self.height = 1

    def push(self,value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.height += 1
            return True
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def Pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = temp.next
        self.height -= 1
        return temp

    def PrintStack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


mynode = Stack(3)
mynode.Pop()
mynode.push(33)
mynode.push(4)
mynode.PrintStack()

def checkforparanthesis(strs):
    open_paran = ['[', '{', '(']
    close_paran = [']', '}', ')']
    stack =[]
    for i in strs:
        if i in open_paran:
            stack.append(i)
        elif i in close_paran:
            pos = close_paran.index(i)
            if len(stack) > 0 and stack[len(stack)-1] == open_paran[pos]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(checkforparanthesis("{[]}"))