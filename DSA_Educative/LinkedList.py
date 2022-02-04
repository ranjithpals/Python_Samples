class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __add__(self, other):
        self.next = other


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Prev Node is not available")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, delete_node):
        if not delete_node:
            print("Node to be deleted does not exist")
            return
        temp = delete_node

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def rotate(self, k):
        curr = self.head
        cnt = 0
        prev = None
        nxt = None
        if self.len_iterative() == k+1:
            return
        while curr:
            prev = curr
            nxt = curr.next
            if cnt == k:
                curr.next = None
            curr = nxt
            cnt += 1
        prev.next = self.head
        self.head = nxt

        # print(prev)

    def move_tail_to_head(self):
        head = self.head
        curr = self.head
        last = None
        prev = None
        if curr is None or curr.next is None:
            print('The flip is not applicable')
            return
        while curr:
            if curr.next:
                prev = curr
            else:
                last = curr
            curr = curr.next
        last.next = self.head
        prev.next = None
        self.head = last

    def reverse(self):
        nxt = None
        prev = None
        curr = self.head
        while curr and curr.next:
            prev = curr
            nxt = curr.next
            prev.next = nxt.next
            nxt.next = self.head
            self.head = nxt


llist = LinkedList()
# llist.append(8)
# llist.append(10)
llist.append(5)
llist.append(7)
llist.append(9)
llist.append(3)

llist.insert_after_node(llist.head.next.next, 7)
llist.print_list()

# llist.rotate(2)
llist.reverse()
llist.print_list()