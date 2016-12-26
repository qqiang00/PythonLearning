"""树结构
"""

class TreeNode(object):
  def __init__(self, data=None, tag=None):
    self.tag = tag
    self.data = data
    self.childs = []
  
  def __str__(self):
    s = "<TreeNode 'tag':'{}', 'data':{}>\n".format(self.tag, self.data)
    for i,child in enumerate(self.childs):
      s += " child" + str(i) + ": " + str(child)
    return s
    
class BTreeNode(TreeNode):
  def __init__(self, data=None, tag=None):
    super().__init__(data, tag)
    self.childs = [None, None]
    
  @property
  def left(self):
    return self.childs[0]
  
  @left.setter
  def left(self, value):
    if not isinstance(value, TreeNode):
      raise TypeError("Expected a TreeNode obejct.")
    self.childs[0] = value
    
  @property
  def right(self):
    return self.childs[1]
  
  @right.setter
  def right(self, value):
    if not isinstance(value, TreeNode):
      raise TypeError("Expected a TreeNode obejct.")
    self.childs[1] = value
    
  def __str__(self):
    s = "<BTreeNode 'tag':'{}', 'data':{}>\n".format(self.tag, self.data)
    s += " left:\t" + str(self.left) + "\n"
    s += " right:\t" + str(self.right) + "\n"
    return s
    
class BTree(object):
  def __init__(self,root):
    if not isinstance(root, BTreeNode):
      raise TypeError("Expected a BTreeNode as a root")
    self.root = root
  
  def __child_path(self, root, target, path_):
    if root is None:
      return False
    path_.append(root)   
    if root is target:
      return True
    found = False
    if root.left is not None:
      found = self.__child_path(root.left, target, path_)
    if found is False and self.root.right is not None:
      found = self.__child_path(root.right, target, path_)
    if found is False:
      path_.pop()
    return found
    
  def child_path(self, target):
    """ 从根节点到某子目标节点的路径
    target：目标节点
    return：返回路径list，如果目标节点不在树中，则返回空list
    """
    path_ = []
    self.__child_path(self.root, target, path_)
    return path_
  
def test_child_path():
  childs = [BTreeNode(i) for i in range(9)]
  root = childs[3]
  tree = BTree(root)
  childs[3].left = childs[5]
  childs[3].right = childs[1]
  childs[5].left = childs[6]
  childs[5].right = childs[2]
  childs[2].left = childs[7]
  childs[2].right = childs[4]
  
  childs[1].left = childs[0]
  childs[1].right = childs[8]
  
  path_ = tree.child_path(childs[4])

  for node in path_:
    print(str(node.data) + " ",end=" ")
  
def test():
  root = TreeNode(data=3, tag="root")
  print(root)
  
  btroot = BTreeNode(data="19", tag="btroot")
  btroot.left = root
  btroot.right = TreeNode(data = 10, tag="right child")
  print(btroot)
  

  
if __name__ == "__main__":
  test_child_path()