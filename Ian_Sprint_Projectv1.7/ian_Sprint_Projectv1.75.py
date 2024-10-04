import cmath

def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root_1 = (-b + (discriminant))/2*a
    root_2 = (-b - (discriminant))/2*a
    return root_1, root_2
  #  if discriminant > 0:

   # elif discriminant == 0:

    #else:
     #   return None

print(calculate_roots(1, 5, 6))
print(calculate_roots(1, 2, 1))