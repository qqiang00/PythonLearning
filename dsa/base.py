"""
Stack.py
"""
from abc import abstractmethod, ABCMeta
from dsa.exceptions import *

class IStack(metaclass=ABCMeta):
  """Stack abstract class (Interface)
  """
  @abstractmethod
  def getSize(self):pass
  @abstractmethod
  def isEmpty(self):pass
  @abstractmethod
  def top(self):pass
  @abstractmethod
  def push(self, ele):pass
  @abstractmethod
  def pop(self):pass;
  
class IQueue(metaclass=ABCMeta):
  @abstractmethod
  def getSize(self):pass
  @abstractmethod
  def isEmpty(self):pass
  @abstractmethod
  def peek(self):pass
  @abstractmethod
  def enqueue(self, ele):pass
  @abstractmethod
  def dequeue(self):pass
  @abstractmethod
  def traversal(self):pass
  
class Queue(IQueue):
  CAPACITY = 1000 # 默认Queue容量
  def __init__(self, capacity=CAPACITY):
    self._items = []
    self._capacity = capacity
  
  @property
  def capacity(self):
    return self._capacity
  
  def getSize(self):
    return len(self._items)
  
  def isEmpty(self):
    return len(self._items) == 0
  
  def peek(self):
    if self.isEmpty():
      raise QueueEmptyException(DSAExceptionMsg.EmptyQueue)
    return self._items[0]
  
  def enqueue(self, ele):
    if self.getSize() == self._capacity:
      raise QueueFullException(DSAExceptionMsg.FullQueue)
    self._items.append(ele)
  
  def dequeue(self):
    if self.isEmpty():
      raise QueueEmptyException(DSAExceptionMsg.EmptyStack)
    item = self._items[0]
    self._items.remove(item)
    return item
  
  def traversal(self):
    s = "Queue: "
    for c in self._items:
      s += str(c) + ", "
    return s
    
class Stack(IStack):
  CAPACITY = 1000 # 默认Stack容量  
  def __init__(self, capacity=CAPACITY):
    self._items = []
    self._capacity = capacity
  
  @property
  def capacity(self):
    return self._capacity
  
  def __str__(self):
    s = "Stack: "
    for c in self._items:
      s += str(c) + ", "
    return s
  
  def getSize(self):
    return len(self._items)
  
  def isEmpty(self):
    return len(self._items) == 0
  
  def top(self):
    if self.isEmpty():
      raise StackEmptyException(DSAExceptionMsg.EmptyStack)
    return self._items[len(self._items)-1]
  
  def push(self,item):
    if self.getSize() == self._capacity:
      raise StackFullException(DSAExceptionMsg.FullStack)
    self._items.append(item)
    
  def pop(self):
    if self.isEmpty():
      raise StackEmptyException(DSAExceptionMsg.EmptyStack)
    return self._items.pop()

def test_Stack():
  s = Stack(10)
  print("Stack Capacity ", s.capacity)
  try:
    s.push(4)
    s.top()
    s.push('dog')
    s.push(True)
    s.push(8.4)
    #s.pop()
    # s.pop()
    print(s)
  except (StackEmptyException, StackFullException) as e:
    print(e.message)
  finally:
    pass
  
if __name__ == "__main__":
  test_Stack()
  

    
  