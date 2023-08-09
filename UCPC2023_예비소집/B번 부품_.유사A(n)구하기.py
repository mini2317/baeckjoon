def f(n):
  if n == 1:
    return 1
  else:
    return f(n-1) + f(1)
print([f(i) for i in range(1,101)])