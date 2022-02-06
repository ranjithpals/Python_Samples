class Node:                         # Class for creating a Node
    def __init__(self, data):
        self.data = data            # Value of the Node
        self.next = None            # Node attached to this node


class CircularLinkedList:           # Class for creating a Circular Linked List
    def __init__(self):
        self.head = None            # Assign empty Node to the Head Node of the CLL

    def append(self, data):         # To Append a new node with a given value (data)
        node = Node(data)           # Create a New Node with given value
        if self.head is None:       # Check if the
            self.head = node
            self.head.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = node
        node.next = self.head

    def print_list(self):
        curr = self.head
        print(curr.data)
        while curr.next != self.head:
            print(curr.next.data)
            curr = curr.next

    def prepend(self, data):
        node = Node(data)
        curr = self.head
        node.next = curr
        if curr is None:
            self.head = node
            return
        while curr.next != self.head:
            curr = curr.next
        curr.next = node
        self.head = node

    def remove(self, key):
        curr = self.head
        if curr.data == key:
            prev = curr
            while curr.next != self.head:
                curr = curr.next
            curr.next = prev.next
            self.head = curr.next
            curr = None
        else:
            prev = None
            remove = None
            while curr.next != self.head:
                prev = curr
                if curr.next.data == key:
                    remove = curr.next
                    break
                curr = prev.next
            if remove.next:
                prev.next = remove.next
            else:
                prev.next = self.head
            remove = None

    def __len__(self):
        count = 0
        curr = self.head
        if curr:
            count = 1
        while curr.next != self.head:
            count += 1
            curr = curr.next
        return count


    def split_1(self, sp_no):
        # Find the length of the CLL
        split_no = 0
        len_cll = len(self)
        split_no = len_cll // sp_no
        if sp_no >= len_cll:
            print('Provide a valid split number')
            return
        prev = None
        curr = self.head
        count = 0
        # Truncate the existing CLL (self)
        while curr and count < split_no:
            prev = curr
            count += 1
            curr = curr.next
        prev.next = self.head

        # Create a New CLL
        cll_1 = CircularLinkedList()
        while curr.next != self.head:
            cll_1.append(curr.data)
            curr = curr.next
        cll_1.append(curr.data)

        return cll_1

    def josephus_problem(self, step):
        # check if length of CLL is greater than 1
        curr = self.head
        prev = None
        while len(self) > 1:
            count = 1
            while count <= step:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = curr.next
            curr = curr.next
            # curr = None




cll = CircularLinkedList()
cll.append(6)
cll.append(8)
cll.append(10)
cll.print_list()

cll.prepend(15)
cll.print_list()

cll.remove(15)
cll.print_list()
l_cll = len(cll)
print(f'Length of Circular Linked List is {l_cll}')

cll.append(2)
cll.print_list()


cll.josephus_problem(2)
print(f'Circular LL after solving the Josephs Problem')
cll.print_list()

'''
c1 = cll.split_1(2)
print('First Split Circular LinkedList')
cll.print_list()
print('Second Split Circular LinkedList')
c1.print_list()
'''


