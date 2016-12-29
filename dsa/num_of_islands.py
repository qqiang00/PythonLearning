"""分别使用深度和广度优先搜索算法计算孤岛问题
"""
from errno import EBADSLT
class Solution(object):
  order = 1
 
  @classmethod
  def reset_order(cls):
    cls.order = 1
    
  def numIslands(self, grid, search_method):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if grid is None or len(grid) == 0:
      return 0
    ans = 0
    m, n = len(grid), len(grid[0])
    visited = [ [False] * n for _ in range(m)]    # label whether a cell is visited
    ordered = [ [0]*n for _ in range(m)]    # 记录遍历顺序
    print("perform search using method:{}".format(search_method.__name__))
    for x in range(m):
      for y in range(n):
        if grid[x][y] == '1' and not visited[x][y]:
          ans += 1
          search_method(grid, visited, ordered, x, y, m, n)
    print("搜索次序（按数字从小到大搜索) 搜索优先级 下->右->上->左")
    for m in range(len(ordered)):
      for n in range(len(ordered[0])):
        print("%3d"%ordered[m][n],end=" ")
      print()
    return ans
        
  def bfs(self, grid, visited, ordered, x, y, m, n):
    #dz = zip([1, 0, -1, 0],[0, 1, 0, -1])
    dz =[(1,0),(0,1),(-1,0),(0,-1)] #搜索次序是 下->右->上->左
    queue = [(x, y)]
    self.visiting(visited, ordered,(x,y))
    while len(queue) > 0:
      target = queue.pop(0)
      for d in dz:
        np = (target[0]+d[0], target[1]+d[1])
        if self.isvalid(np, m, n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
          self.visiting(visited, ordered, np)
          queue.append(np)
    
  def dfs(self, grid, visited, ordered, x, y, m, n):
    self.visiting(visited, ordered, (x,y))
    dz = [(1,0),(0,1),(-1,0),(0,-1)]  # 搜索次序是 下->右->上->左
    for d in dz:
      np = (x + d[0], y + d[1])
      if self.isvalid(np, m, n) and grid[np[0]][np[1]] == "1" and not visited[np[0]][np[1]]:
        self.dfs(grid, visited, ordered, np[0], np[1], m, n)
        
  def isvalid(self, np, m ,n):
    return 0 <= np[0] < m and 0 <= np[1] < n
      
  def visiting(self, visited, ordered, p):
    # print("{0:2d}th visit: {1[1]:2d},{1[0]:2d}".format(self.order,p))
    ordered[p[0]][p[1]] = self.order
    self.order += 1
    visited[p[0]][p[1]] = True
    
  def print_visited(self,visited):
    for c in range(len(visited)):
      print(visited[c])
      
if __name__ == "__main__":
  grid =["1110001001",
         "1110001101",
         "1100100000",
         "1111100111",
         "0000001000",
         "0011100001",
         "1000001000"]
        
  slt = Solution()
  print("原始数据:")
  for m in range(len(grid)):
    for n in range(len(grid[0])):
      print("%3s" % grid[m][n],end=" ")
    print()
  print()

  ans = slt.numIslands(grid,slt.bfs)
  print("number of island is:%s\n" % ans)
  slt.order = 1
  ans = slt.numIslands(grid,slt.dfs)
  print("number of island is:%s" % ans)
  
  
  
  
  
        