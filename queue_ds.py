
#making queue class for voting system
class Queue:
    #implementation using list
    def __init__(self):
        self.queue = []

    #enqueue adds to the back
    def enqueue(self, item):
        self.queue.append(item)

    #dequeue removes from front (if not empty)
    #if empty raises error
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    #check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    #peek returns the front item (w/o removing it)
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")
    
    #return the number of items
    def __len__(self):
        return len(self.queue)
    