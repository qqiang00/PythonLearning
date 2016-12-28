"""树结构
"""
class TreeNode(object):
  """一般树的节点"""
  
  def __init__(self, value=None, tag=None):
    self.tag = tag
    self.value = value
    self.children = []
  
  def __iter__(self):
    return iter(self.children)
  
  def __repr__(self):
    return "TreeNode({},{})".format(self.value,self.tag)
  
  def __str__(self):
    return "<TreeNode value:{} {}, tag:{}>".format(
      self.value, type(self.value), self.tag)
    
class BTreeNode(TreeNode):
  """二叉树节点类"""
  
  def __init__(self, value=None, tag=None):
    """初始化，子节点有最多有2个，left和right"""
    super().__init__(value, tag)
    self.children = [None, None]
    
  @property
  def left(self):
    """获取左子节点"""
    return self.children[0]
  
  @left.setter
  def left(self, value):
    """设置左子节点(必须是BTreeNode类型或None)"""
    if value is not None and not isinstance(value, BTreeNode):
      raise TypeError("{} is not a BTreeNode obejct.".format(value))
    self.children[0] = value
    
  @property
  def right(self):
    """获取右子节点"""
    return self.children[1]
  
  @right.setter
  def right(self, value):
    """设置右子节点(必须是BTreeNode类型或None)"""
    if value is not None and  not isinstance(value, BTreeNode):
      raise TypeError("{} is not a BTreeNode obejct.".format(value))
    self.children[1] = value
    
  def __str__(self):
    return "<BTreeNode value:{} {}, tag:{}>".format(
      self.value, type(self.value), self.tag)
    
  def inorder_traversal(self):
    """中序遍历节点子树"""
    if self.left is not None:
      yield from self.left.inorder_traversal()
    yield self
    if self.right is not None:
      yield from self.right.inorder_traversal() 
    
  def preorder_traversal(self):
    """前序遍历节点子树"""
    yield self
    if self.left is not None:
      yield from self.left.preorder_traversal()
    if self.right is not None:
      yield from self.right.preorder_traversal()   
  
  def postorder_traversal(self):
    """后序遍历节点子树"""
    if self.left is not None:
      yield from self.left.postorder_traversal()
    if self.right is not None:
      yield from self.right.postorder_traversal()       
    yield self
    
  def level_order_traversal(self):
    """层次遍历节点子树"""
    if self is not None:
      queue = [self]
      while len(queue) > 0:
        yield queue[0]
        p = queue[0]
        queue.remove(p)
        for c in p.children:
          if c is not None:
            queue.append(c)
               
        
class BTree(object):
  """implemention of Binary Tree 
  二叉树定义
  """
  
  def __init__(self,root:BTreeNode = None):
    if not isinstance(root, BTreeNode):
      raise TypeError("Expected a BTreeNode as a root")
    self._root = root

  
  @staticmethod
  def _create_root(arr:list, index:int=0) -> BTreeNode:
    """create a complete binary tree using givin arr[index:]
    Returns: root of the tree
    """
    if arr is None or index >= len(arr):
      return None
    root = BTreeNode(arr[index])
    root.left = BTree._create_root(arr, 2*index+1)
    root.right = BTree._create_root(arr, 2*(index+1))
    return root
     
  @classmethod
  def build_from_array(cls, arr):
    """从一个数组构建一个二叉树"""
    root = BTree._create_root(arr)
    return cls(root)
 
  @property
  def root(self):
    """返回树的根(节点)"""
    return self._root
  
  def is_empty(self):
    """判断树是否为空: True if tree is empty, False if not
    """
    return self._root is None
  
  def inorder_traversal(self):
    """中序遍历树(根节点)"""
    return self._root.inorder_traversal()
  
  def preorder_traversal(self):
    """前序遍历节点子树"""
    return self._root.preorder_traversal()
  
  def postorder_traversal(self):
    """后序遍历节点子树"""
    return self._root.postorder_traversal()
    
  def level_order_traversal(self):
    """层次遍历节点子树"""
    return self._root.level_order_traversal()
     
  @staticmethod
  def __child_path(root, target, path_):
    if root is None or target is None:
      return False
    path_.append(root)   
    if root is target:
      return True
    found = False
    if root.left is not None:
      found = BTree.__child_path(root.left, target, path_)
    if found is False and root.right is not None:
      found = BTree.__child_path(root.right, target, path_)
    if found is False:
      path_.pop()
    return found
    
  def child_path(self, target):
    """ 从根节点到某子目标节点的路径
    target：目标节点
    return：返回路径list，如果目标节点不在树中，则返回空list
    """
    if target is None or self.root is None:
      return []
    path_ = []
    BTree.__child_path(self.root, target, path_)
    return path_
  