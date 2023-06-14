t = 0.1;
y = 0;


def height(v0, t):
  g = 32.8
  y = (v0*t - 0.5*g*t**2)
  return y

while t > 0:

  v0 = input('Input velocity: ')
  v0 = float(v0)
  
  while y >= 0:
    y = height(v0,t)
    print(f"t = {t}")
    print("%.2f" % y)
    t = t + 0.1
    

  

