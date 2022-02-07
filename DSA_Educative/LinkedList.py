class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __add__(self, other):
        self.next = other


class LinkedList:                   # Create a New Linked List
    def __init__(self):             # Create a Null head
        self.head = None

    def append(self, data):         # Append a new Node to the Linked List LL
        new_node = Node(data)       # Create a New Node
        if self.head is None:       # If Head node of LL is Null
            self.head = new_node    # Head node is New Node
            return                  # Function return
        last_node = self.head       # last node is head node
        while last_node.next:       # Check if next node is available
            last_node = last_node.next  # Traverse to the next node
        last_node.next = new_node   # Assign new node to follow the last node of LL

    def prepend(self, data):        # Prepend the node
        new_node = Node(data)       # Create a New Node with data value
        new_node.next = self.head   # Assign new node's next to Head Node
        self.head = new_node        # Head node of LL is new Node

    def print_list(self):           # Print the list of nodes of LL
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def insert_after_node(self, prev_node, data):   # Insert the new node after given node
        if not prev_node:                           # Check if the given node exists
            print("Prev Node is not available")
            return
        new_node = Node(data)                       # Create New node
        new_node.next = prev_node.next  # New nodes next is assigned to given node next
        # this is so that we do not loose the link to the Node next to the new node
        prev_node.next = new_node       # given nodes next is assigned to New Node

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