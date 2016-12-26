class DSAExceptionMsg(object):
  EmptyStack = "Error: Empty Stack.";
  FullStack = "Error: Stack is full.";
  FullQueue = "Queue overflow.";
  EmptyQueue = "Empty Queue.";


class QueueEmptyException(Exception):
  pass
  #def __init__(self, message=None, status=None):
  #  super().__init__(message, status)
  #  self.message = message
  #  self.status = status
    
class QueueFullException(Exception):
  pass
  #def __init__(self, message=None, status=None):
  #  super().__init__(message, status)
  #  self.message = message
  #  self.status = status
    
class StackEmptyException(Exception):
  pass
  #def __init__(self, message=None, status=None):
  #  super().__init__(message, status)
  #  self.message = message
  #  self.status = status
    
class StackFullException(Exception):
  pass
  #def __init__(self, message=None, status=None):
  #  super().__init__(message, status)
  #  self.message = message
  #  self.status = status