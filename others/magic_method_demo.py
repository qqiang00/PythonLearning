"""这个示例演示了Python里的一些魔术方法的使用
"""

from os.path import join

# __init__ 和 __del__ 一起工作的例子
class FileObject(object):
  def __init__(self, filepath='~', filename='sample.txt'):
    self.file = open(join(filepath,filename),'r+')
    
  def __del__(self):
    self.file.close()
    del self.file
    
# __eq__, __ne__, __lt__, __gt__ 方法
class Word(str):
  '''存储单词的类，定义比较单词的几种方法
  '''
  def __new__(cls, word):
    # 注意，我们必须要用到 __new__方法，因为str是不可变类型
    # 所以，我们必须在创建的时候将它初始化
    if ' ' in word:
      print("Value contains spaces. Truncating to first space.")
      word = word[:word.index(' ')] # 单词是第一个空格之前的所有字符
    return str.__new__(cls,word)
  
  def __gt__(self,other):
    return len(self) > len(other)
  def __lt__(self, other):
      return len(self) < len(other)
  def __ge__(self, other):
      return len(self) >= len(other)
  def __le__(self, other):
      return len(self) <= len(other)  
    
    

