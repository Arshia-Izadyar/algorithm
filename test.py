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
    def display(self):
        arr = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            arr.append(cur.data)
        print(arr)
        
    def length(self):
        cur = self.head
        c = 0
        while cur.next != None:
            cur = cur.next
            c += 1
        return c
    def erase(self, num):
        cur = self.head
        while cur.next != None:
            last = cur
            cur = cur.next
            if cur.data == num:
                last.next = cur.next
                return
    def erase_at(self, i):
        index = 0
        cur = self.head
        if i >= self.length():
            raise IndexError("Out of range")
        while True:
            last = cur
            cur = cur.next
            if i == index:
                last.next = cur.next
                return
            index += 1
            
    def get_at(self, i):
        indx = 0 
        cur = self.head
        if i >= self.length():
            raise IndexError("Out of range")
        while True:
            cur = cur.next
            if i == indx:
                
                return cur.data
            indx += 1
            
    def get(self, num):
        cur = self.head
        i = 0
        while cur.next != None:
            cur = cur.next
            if cur.data == num:
                return cur.data, i
            i += 1
            
                

                

def main():
    # print(binarySearch([31, 34 ,45, 23, 55, 12, 14, 98, 21], 98))
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(4)
    li.append(5)
    li.append(6)
    print(li.length())
    li.display()

    li.erase_at(3)
    li.erase(3)

    li.display()
    
    


if __name__ == "__main__":
    main()
