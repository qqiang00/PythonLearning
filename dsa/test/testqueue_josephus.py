from dsa.base import Queue

def Josephus(q, k):
  if q.isEmpty():
    return None
  while q.getSize() > 1:
    print(q.traversal())
    for _ in range(k):
      q.enqueue(q.dequeue())
    e = q.dequeue()
    print(" {} 退出".format(e))
  return q.dequeue()

def buildQueue(arr):
  q = Queue()
  for a in arr:
    q.enqueue(a)
  return q

if __name__ == "__main__":
  kids = ["Alice", "Bob", "Cindy", "Fred", "Gene", "Hope", "Kim",
      "Lance", "Mike", "Doug", "Irene", "Nancy", "Ed", "Jack", "Ollie"]
  luckiest_kid = Josephus(buildQueue(kids), 5)
  print("最终的幸运者是: {}".format(luckiest_kid))