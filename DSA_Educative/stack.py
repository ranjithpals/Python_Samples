class Stack:


    def __init__(self):
        self.st = []

    def push(self, elem):
        self.st.append(elem)

    def pop(self):
        return self.st.pop()

    def is_empty(self):
        return self.st == []

    def peek(self):
        if not self.is_empty():
            return self.st[-1]

    def get_stack(self):
        return self.st
