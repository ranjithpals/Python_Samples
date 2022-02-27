# Creating a Node for the Double Linked List
class Node:
    # Initializing a Node with links for Next and Previous Node
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    # Initialize a Doubly Linked List
    def __init__(self):
        self.head = None

    # Append a Node to the DLL
    def append(self, data):
        node = Node(data)       # Create a New Node
        prev = None             # Variable to hold the previous Node
        curr = self.head        # Assign variable curr to head node
        if curr is None:        # Validate if the DLL is empty
            self.head = node    # Assign the new node as the head node
            return              # Return the function
        prev = curr             # Assign the curr node to variable prev before iteration begins
        while curr.next:     # Check if curr's next node is not null
            prev = curr         # Store the current node
            curr = curr.next    # Parse to the next Node
        curr.next = node        # Assign new node to the curr node's next
        node.previous = prev    # Assign new node's previous to prev node

    # Add a Node to the start of the DLL
    def prepend(self, data):
        node = Node(data)       # Create a New Node
        curr = self.head        # Assign variable curr to head node
        if curr is None:        # Validate if the DLL is empty
            self.head = node    # Assign the new node as the head node
            return              # Return the function
        prev_head = curr        # Assign the existing curr node to variable prev_head
        node.next = prev_head   # Assign new node's next as prev_head
        prev_head.previous = node   # prev_head previous is new node
        self.head = node        # new node is DLL's head

    # Print the list of the Nodes of DLL
    def print_list(self):
        curr = self.head
        if curr is None:        # if the DLL is empty
            print(f'The Double Linked List is empty')
        # prev = curr
        while curr:     # Check if curr is not None
            curr_val = curr.data    # Hold the value of the curr node
            try:                    # If the Pre Node exists hold the node's value
                prev_val = curr.previous.data
            except:
                prev_val = None     # Else assign it as None
            try:
                next_val = curr.next.data # If the Next Node exists hold the node's value
            except:
                next_val = None     # Else assign it as None
            print(f'Node Value:{curr_val}, Prev and Next{prev_val, next_val}')
            curr = curr.next        # Parse to the next node

    # Add a new node before the node with the given key
    def add_before_node(self, key, data):
        node = Node(data)       # Create a New Node
        curr = self.head        # Assign variable curr to head node
        if curr is None:        # Validate if the DLL is empty
            self.head = node    # Assign the new node as the head node
            return              # Return the function
        while curr.next:        # Check if next node exists
            prev = curr         # Assign curr node to var prev
            nxt = curr.next     # Assign curr.next to var nxt
            if curr.next.data == key:   # check if curr.next value is key
                prev.next = node    # prev next => node
                node.previous = prev    # node prev => prev
                node.next = nxt     # node next => nxt
                nxt.previous = node     # nxt previous => node
                return
            curr = curr.next
        prev.next = node
        node.previous = prev

    # Reverse a DLL
    def reverse(self):
        tmp = None          # tmp variable to capture previous value
        curr = self.head    # assign the head node
        while curr:         # if curr exists
            tmp = curr.previous     # assign the previous to curr node
            curr.previous = curr.next   # curr prev => curr next
            curr.next = tmp     # curr next => curr previous
            curr = curr.previous    # Parse curr => curr prev as next is already assigned to prev
        if tmp:
            self.head = tmp.previous    # assign the last node as self head

    # Find Pairs adding up to 5 in DLL
    def add_pairs(self, sum_val):
        lst = []
        result = []
        curr = self.head
        while curr:
            lst.append(curr.data)
            rem = sum_val - curr.data
            if rem in lst:
                elem = f'({rem},{curr.data})'
                result.append(elem)
                lst.remove(rem)
                lst.remove(curr.data)
            curr = curr.next
        return result


if __name__ == "__main__":
    # Create a New Doubly Linked List
    dll = DoublyLinkedList()
    # Add a new node to the DLL
    dll.append(25)
    dll.append(13)
    dll.append(3)
    dll.prepend(21)
    # dll.print_list()
    '''
    print("New Test Case")
    dllist = DoublyLinkedList()
    dllist.prepend(0)
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.prepend(5)
    '''
    dll.add_before_node(3, 10)

    # dll.reverse()
    # dll.print_list()
    pairs = dll.add_pairs(13)
    print(pairs)




