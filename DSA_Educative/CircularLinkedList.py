class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
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

    def split(self, sp_count):

        len_clist = len(self)
        trunc_size = len_clist//sp_count
        print(trunc_size)

        if sp_count >= len_clist:
            print(f'Length of Circular Linked list is {len_clist}, provide a correct number')
            return
        else:
            curr = self.head
            nxt = None
            count = 0
            # Create a Circular Linked List
            cll_1 = CircularLinkedList()
            cll_2 = CircularLinkedList()
            cll_1.head = curr
            count += 1
            while curr.next and count < trunc_size:
                cll_1.append(curr.next.data)
                count += 1
                curr = curr.next
            nxt = curr
            # curr.next = cll_1.head
            cll_2.head = nxt
            count = 0
            while nxt.next and count < trunc_size:
                cll_2.append(nxt.next.data)
                count += 1
                nxt = nxt.next
            # nxt.next = cll_2.head
            return cll_1, cll_2




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
c1, c2 = cll.split(2)
print('Two Split Circular LinkedList')
c1.print_list()
c2.print_list()

