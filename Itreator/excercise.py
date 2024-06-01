class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  def traverse_preorder(self):
      yield self.value

      if self.left:
        yield from self.left.traverse_preorder()
      
      if self.right:
        yield from self.right.traverse_preorder()
    
 
if __name__ == '__main__':
  #   1
  #  / \
  # 2   3

  # in-order: 213
  # preorder: 123
  # postorder: 231

  node = Node('a',
                Node('b',
                     Node('c'),
                     Node('d')),
                Node('e'))

  node.traverse_preorder()
