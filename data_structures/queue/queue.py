from node import Node


class Queue:
    def __init__(self, max_size=0):
        self.max_size = max_size
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print('No more room!')

    def deqeue(self):
        if not self.has_space():
            item_to_remove = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()

        else:
            print('This queue is empty!')

    def peek(self):
        if self.size <= 0:
            return "Nothing to see here!"
        return self.head.get_value()

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        return self.max_size > self.get_size()

    def is_empty(self):
        return self.get_size() == 0
