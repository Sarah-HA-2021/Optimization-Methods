def grad_descent(f, x0, rate, max_iterations=100, eps=1e-4):
  all_x = [x0]
  cur_x = x0
  for i in range(max_iterations+1):
    # df_approx = (f(cur_x + eps) - f(cur_x)) / eps
    df_approx = (f(cur_x + eps/2) - f(cur_x-eps/2)) / eps
    new_x = cur_x - rate * df_approx
    all_x.append(new_x)
    cur_x = new_x
  return all_x
