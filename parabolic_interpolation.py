import math 
def minimize_parabolic(f,x1,x2,x3,eps):
  x4=0
  iterations=0
  while (abs(x3 - x1)> eps and iterations<100):
   fx1=f(x1)
   fx2= f(x2)
   fx3=f(x3)
   #print(x1,x2,x3)
   try:
    l= (math.pow(x2-x1,2)) *(fx2-fx3) - (math.pow(x2-x3,2)) *(fx2-fx1) 
    p= (math.pow(x2-x1,1)) *(fx2-fx3) - (math.pow(x2-x3,1)) *(fx2-fx1) 
    x4= x2- 0.5 *(l/p)
    fx4=f(x4)
   except:
     break
   if(fx4>fx2):
     x1=x2
     x2 = x4
   else:
      x3=x2
      x2=x4
   fx1=f(x1)
   fx2= f(x2)
   fx3=f(x3)
   #print(x4)
   iterations=iterations+1
  return fx2 , iterations
