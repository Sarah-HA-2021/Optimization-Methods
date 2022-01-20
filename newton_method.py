from math import sin, cos
tol = 0.0001
x_init = 1.0 
y_init = -1.0
f = lambda x, y: cos(x*y)-0.5
g = lambda x, y: sin(x+y)-0.3


import numpy as np 

def norm (x1,x2):
  sum =0 
  for i in range (0,2):
    sum = sum + abs(x2[i]-x1[i])
  return round(sum[0] ,10)


def grad_x_approximation(f,cur_x,y,eps=10-9):
  return (f(cur_x + eps/2,y) - f(cur_x-eps/2,y)) / eps

def grad_y_approximation(f,cur_x,y,eps=10-9):
  return (f(cur_x ,y+ eps/2) - f(cur_x,y-eps/2)) / eps

#numpy.linalg.norm(xkplus1-xk) > tol   and
import numpy as np
def solve (f,g,x_init,y_init,tol,iter_max=1000):
  x= x_init
  y= y_init
  xk = [[x],[y]]
  xk=np.array(xk)
  #xkplus1=np.array([[1000000000000],[10000000000]])
  iter=0
  Fxk=[[f(x,y)],[g(x,y)]]
  Fxk = np.array(Fxk)
  #print(xk.shape,Fxk.shape)
    #print(Fxk)
  Jac =  [ [ grad_x_approximation(f,x,y)  ,grad_y_approximation(f,x,y)  ]  , [  grad_x_approximation(g,x,y)  ,grad_y_approximation(g,x,y)          ]                      ]
  Jac  = np.array(Jac)
  Fxkminus = -1* Fxk
  #print("Jac",Jac)
  deltaxk=  np.matmul(np.linalg.inv(Jac),  Fxkminus )
  xkplus1=  deltaxk + xk 
    #print(xk)
  xk =  xkplus1
  x=float(xk[0])
  y=float(xk[1])
  #print(x,y)
  iter= iter+1
  while ( iter <iter_max):
    #print (xk)
    #print("yes")
    Fxk=([f(x,y)],[g(x,y)])
    Fxk = np.array(Fxk)
    #print(Fxk)
    Jac =  [ [ grad_x_approximation(f,x,y)  ,grad_y_approximation(f,x,y) ]  , [  grad_x_approximation(g,x,y)  ,grad_y_approximation(g,x,y)       ]                      ]
    #Jac  = np.array(Jac)
    Fxkminus = -1* Fxk
    #print("jAC",Jac)
    deltaxk=  np.matmul(np.linalg.inv(Jac),  Fxkminus )
    xkplus1=  deltaxk + xk 
    #print(xk)
    xk =  xkplus1
    x=float(xk[0])
    y=float(xk[1])
    iter= iter+1
    #fxk = 
   #print(x[0] , y[0] )
  print ('%.7f'%x , '%.7f'%y )
solve(f,g,x_init,y_init,tol)
