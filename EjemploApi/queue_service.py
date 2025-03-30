class Node:
    def __init__(self, data: dict):
        self.data = data
        self.next = None

class QueueService:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data: dict):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self) -> dict:
        if not self.front:
            return None
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return temp.data

    def list_all(self) -> list:
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result