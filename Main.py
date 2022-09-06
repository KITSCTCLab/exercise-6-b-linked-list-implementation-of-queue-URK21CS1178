class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
     # allocate the node in a heap
        node = Node(item)
        print('Inserting…', item)
 
        # special case: queue was empty
        if self.front is None:
            # initialize both front and rear
            self.front = node
            self.rear = node
        else:
            # update rear
            self.rear.next = node
            self.rear = node
 
        # increase the node's count by 1
        self.count += 1
 
    # Utility function to return the top element in a queue

  def dequeue(self) -> None:
    # Write your code here
 if self.front is None:
            print('Queue Underflow')
            exit(-1)
 
        temp = self.front
        print('Removing…', temp.data)
 
        # advance front to the next node
        self.front = self.front.next
 
        # if the list becomes empty
        if self.front is None:
            self.rear = None
 
        # decrease the node's count by 1
        self.count -= 1
 
        # return the removed item
        return temp.data
 

  def status(self) -> None:
    # Write your code here
     
if __name__ == '__main__':
 
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
 
    print('The front element is', q.peek())
 
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
 
    if q.isEmpty():
        print('The queue is empty')
    else:
        print('The queue is not empty')
 


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
