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
      if(is_full(q)) {
  printf("Queue Overflow\n");
}
else {
  q->Q[q->tail] = x;
  if(q->tail == q->size)
    q->tail = 1;
  else
    q->tail = q->tail+1;
}
}
        
  def dequeue(self) -> None:
    # Write your code here
    if(is_empty(q)) {
  printf("Underflow\n");
  return -1000;
}
else {
  int x = q->Q[q->head];
  if(q->head == q->size) {
    q->head = 1;
  }
  else {
    q->head = q->head+1;
  }
  return x;
}
}
        
  
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
