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
      temp = Node(item)
          
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        
  def dequeue(self) -> None:
    # Write your code here
         return
        temp = self.front
        self.front = temp.next
  
        if(self.front == None):
            self.rear = None
  
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
