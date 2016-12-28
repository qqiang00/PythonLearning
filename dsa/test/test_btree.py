from dsa.tree import BTreeNode, BTree
from dsa.tree import TreeNode
from distutils.command.build import build

def build_btree():
  """构建一个二叉树
              3
            /  \     
           5    1
         / \   / \
        6  2  0  8
          / \
         7  4
  """
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
  return tree

def test_child_path(tree, child):
  if child is None:
    print("can not find a None node in a tree.")
    return 
  path_ = tree.child_path(child)
  print("find path for node {} in tree:".format(child.value), end=" ")
  for node in path_:
    print(str(node.value) + " ",end=" ")
  print()
  
def test_traversal(tree, traversal_method):
  print(traversal_method.__name__ +":\t", end=" ")
  for c in traversal_method():
    print(c.value, end = " ")
  print()
  
if __name__ == "__main__":
  #tree = build_btree()
  tree = BTree.build_from_array([3, 5, 1, 6, 2, 0, 8, 7, 4])
  child = tree.root.left.right.right
  test_child_path(tree, child)
  test_traversal(tree, tree.preorder_traversal)
  test_traversal(tree, tree.inorder_traversal)
  test_traversal(tree, tree.postorder_traversal)
  test_traversal(tree, tree.level_order_traversal)
  
  
  
  