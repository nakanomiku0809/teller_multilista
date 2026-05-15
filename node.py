class Node:
    def __init__(self, id, name):
        self.id = str(id).strip()
        self.name = str(name).strip()
        self.next = None
        self.prev = None
        self.sub_list = None

    def __str__(self):
        return self.id + " - " + self.name
