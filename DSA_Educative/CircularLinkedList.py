class Node:                         # Class for creating a Node
    def __init__(self, data):
        self.data = data            # Value of the Node
        self.next = None            # Node attached to this node


# Circular Linked List A -> B -> C -> D -> A, the last node is connected back to the Head
class CircularLinkedList:           # Class for creating a Circular Linked List
    def __init__(self):
        self.head = None            # Assign empty Node to the Head (Node) of the CLL

    def append(self, data):         # To Append a new node with a given value (data) to the end
        node = Node(data)           # Create a New Node with given value
        if self.head is None:       # Check if the Head is empty, if Yes
            self.head = node        # Assign new node to Head
            self.head.next = self.head  # Create circular reference to the head node
            return
        curr = self.head            # Assigning the Head to curr variable
        while curr.next != self.head:   # Check if the next Node is same as head, if so has reached the last node
            curr = curr.next        # Until it has not reached, traverse to the next Node
        curr.next = node            # Adding the new node to be the node following the last node of the CLL
        node.next = self.head       # Assigning the Head node as the node next to the new node added

    def print_list(self):           # Print the nodes of the CLL
        curr = self.head            # Assigning the Head to curr variable
        print(curr.data)            # Print the curr node data
        while curr.next != self.head:   # Check if the next Node is same as head, if so has reached the last node
            print(curr.next.data)   # Print the curr node data
            curr = curr.next        # Traverse to the next node

    def prepend(self, data):        # Add a new node before the head of the CLL
        node = Node(data)           # Create a new node
        curr = self.head            # Assigning the Head to curr variable
        node.next = curr            # Assigning new node's next node as head
        if curr is None:            # Need to connect last node to make it circular
            self.head = node        # If curr node is None, then new node becomes head
            return                  # End the function
        while curr.next != self.head:   # Check if the next Node is same as head, if so has reached the last node
            curr = curr.next        # Traverse to the next node
        curr.next = node            # Last Node linked to new node
        self.head = node            # New Node is the head

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


    def split(self, sp_no):         # Split the CLL into number of CLL's based on the given input
        len_cll = len(self)         # Find the length of the original CLL
        split_no = len_cll // sp_no     # Find the length of the split the CLL's
        if sp_no >= len_cll:        # Check if the length of the split is greater than the original split
            print('Provide a valid split number')   # Not a valid split
            return                  # End the function
        prev = None                 # Variable to capture the node previous to the current node
        curr = self.head            # Assign Head to current node
        count = 0                   # Count the number of nodes traversed
        # Truncate the existing CLL (self)
        while curr and count < split_no:    # Check if the next Node is same as head, if so has reached the last node
            prev = curr             # Assign curr (current) node to Prev before assigning next node to curr
            count += 1              # Increase the count of nodes
            curr = curr.next        # Traverse to the next node
        prev.next = self.head       # Current node (end of first new CLL) linked to head node
        # Create a New CLL
        cll_1 = CircularLinkedList()    # Create New CLL
        while curr.next != self.head:   # Check if the next Node is same as head, if so has reached the last node
            cll_1.append(curr.data)     # Append next node (after last CLL node) to the new CLL
            curr = curr.next            # Traverse to the next node
        cll_1.append(curr.data)         # Append the last node to the new CLL
        return cll_1                    # return the new CLL

    def josephus_problem(self, step):   # Delete the node on which the control lands after n steps from the head
        # Keep deleting the nodes till we have only one node remaining
        curr = self.head
        prev = None                 # Assign Head to current node
        while len(self) > 1:        # check if length of CLL is greater than 1
            count = 1               # counter for number of steps
            while count <= step:    # Check if number of steps is lesser than counter
                prev = curr         # Assign curr (current) node to Prev before assigning next node to curr
                curr = curr.next    # Traverse to the next node
                count += 1          # Increase the counter by 1
            prev.next = curr.next   # Assign the next node of prev to node after current (curr)
            curr = curr.next        # Traverse to the next node (node next to current)





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


