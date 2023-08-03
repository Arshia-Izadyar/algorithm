import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(data)
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        cur = self.head
        li = []
        while cur.next != None:
            cur = cur.next
            li.append(cur.data)
        print(li)
        
    def get_at(self, index):
        if index >= self.length():
            raise IndexError("Index out of range")
        cur = self.head
        i = 0
        while True:
            cur = cur.next
            if i == index : return cur.data
            i += 1
    
    def erase_at(self, index):
        if index >= self.length():
            raise IndexError("index out of range")
        i = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if i == index: 
                last_node.next = cur.next
                return
            i += 1
    def get(self, data):
        cur = self.head
        i = 0
        while cur.next != None:
            cur =cur.next
            if cur.data == data:
                return i, cur.data
            i += 1
            
    def erase(self, data):
        cur = self.head
        while cur.next != None:
            last = cur
            cur = cur.next
            if cur.data == data:
                last.next = cur.next
                return
            
    
    
if __name__ == "__main__":
    my_list1 = LinkedList()
    my_list2 = LinkedList()
    for _ in range(10):
        my_list1.append(random.randint(1, 15))
        my_list2.append(random.randint(1, 15))
    
        
    my_list1.display()
    my_list2.display()

    print(my_list1.get(5))
    print(my_list2.get_at(5))
    my_list1.erase_at(4)
    my_list2.erase(4)
    

    
    
    my_list1.display()
    my_list2.display()
    print("length1 : ",my_list1.length())
    print("length2 : ",my_list2.length())