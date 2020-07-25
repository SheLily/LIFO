from pprint import pprint

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def isEmpty(self):
        if self.head:
            return False
        else:
            return True
        
    def push(self, value):
        new = Node(value, self.head)
        self.head = new
        self.size += 1
        
    def pop(self):
        if self.head:
            temp = self.head
            self.head = self.head.next_node
            self.size -= 1
            return temp.value
        return None
    
    def peek(self):
        if self.head:
            return self.head.value
        else:
            return None
    
    def size(self):
        return self.size
    
        
def is_balanced(brackets):
    samples = {'{': '}', '(':')', '[': ']'}
    stck = Stack()
    for bracket in brackets:
        if bracket in samples:
            stck.push(bracket)
        else:
            if stck.isEmpty():
                return False
            if samples[stck.peek()] == bracket:
                stck.pop()
            else:
                return False
    return True

if __name__ == '__main__':
    brackets_list = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]',
    ]
    
    for brackets in brackets_list:
        print(is_balanced(brackets))
