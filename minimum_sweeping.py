import numpy as np 
def optimize_with_sweep(f, left, right, eps):
  # replace “pass” with your code:
  #pass
  return min(f(x) for x in np.linspace(left, right, int(2*(right-left)/eps)))
  

if __name__ == "__main__":
  #some test cases 

  import math
  # sqrt(x)
  print("minimum of sqrt(x) on [1,2] is: ",optimize_with_sweep(math.sqrt, 1, 2, 0.1))

  # sin(x) between 1 and 100 
  print("minimum of sin(x) on [1,100] is: ", optimize_with_sweep(np.sin, 1, 100, 0.1))

  def f(x):
    return 1/x 

  # 1/x between 1 and 2 
  print("minimum of (1/x) on [1,2] is:" , optimize_with_sweep(f, 1, 2, 0.1))
  # 1/x between -1 and 2 
  print("minimum of (1/x) on [-1,2] is:" ,optimize_with_sweep(f, -1, 2, 0.1))

  # the function f should be continiuos on the range [left,right] to make sweep method work with good presicion 
print("the function f should be continiuos on the range [left,right]  to make sweep method work with good presicion ")
