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
      new_node = Node(value)
        # if empty, assign new node to head and tail
        if self._size == 0:
            self._head = new_node
        # if not empty, make the tail reference the new node
        # so that the new node will become the tail
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1
        
  def dequeue(self) -> None:
    # Write your code here
 if self._size == 0:
            raise Exception("Queue is empty")

        val = self._head.value          # the value to be return
        self._head = self._head.next    # remove the head
        self._size -= 1                 # decrease the size by 1
        return val
  
  def status(self) -> None:
    # Write your code here
    int i;
for(i=q->head; i<q->tail; i++) {
  printf("%d\n",q->Q[i]);
  if(i == q->size) {
    i = 0;
  }
}
}
     
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
