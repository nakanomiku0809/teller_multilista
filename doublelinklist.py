class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def add_child(self, parent, child):
        if parent.sub_list is None:
            parent.sub_list = DoubleLinkedList()

        parent.sub_list.append(child)

    def print_multilist(self, level=0):
        current = self.head

        while current is not None:
            print("  " * level + str(current))

            if current.sub_list is not None:
                current.sub_list.print_multilist(level + 1)

            current = current.next
