class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueService:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, customer):
        new_node = Node(customer)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def list_pending(self):
        customers = []
        current = self.front
        while current:
            customers.append(current.data)
            current = current.next
        return customers