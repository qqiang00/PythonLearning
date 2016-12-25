'''
  a soigmoid regression output layer
'''

from nnlib.funcs import *
import nn.base.funcs as funcs
import nn.base.layer as layer

# sigmoid_reg class is very like the layer where the only difference is the
# activate function is supposed to choose "sigmoid" function
class sigmoid_reg(layer):

  @staticmethod
  def init(presize=1, outsize=1):
    return super().init(presize, outsize)

  @staticmethod
  def forward(in_data,w,userless_parameter):

    output, cache = super().forward(in_data, w, func_name = "sigmoid")
    return output, cache

  @staticmethod
  def backward(dy, cache):
    return super().backward(dy, cache)


if __name__ == "__main__":
  func_list = ["sigmoid", "tanh", "relu", "linear", "softplus"]
  funcs.gradient_check(sigmoid_reg,func_list,1e-5)
