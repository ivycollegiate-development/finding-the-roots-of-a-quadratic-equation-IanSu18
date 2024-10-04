import cmath

def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root_1 = (-b + (discriminant)**(1/2))/(2*a)
    root_2 = (-b - (discriminant)**(1/2))/(2*a)
    return root_1, root_2
  #if discriminant > 0:
    #print(f'There are two real distinct roots, {root_1} and {root_2}'
    #elif discriminant == 0:
      #print(f'There is one real repeated root, {root_1}')
    #else:
       #return None

print(calculate_roots(1, 5, 6))
print(calculate_roots(1, 2, 1))