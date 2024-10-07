import cmath
def get_quadratic_coefficients():
  try:
    coefficients = input('Please enter the coefficient in order.(ex: a b c)')
    a, b, c = map(float, coefficients.split())
    if a == 0:
      print("The first coefficient must not be a zero., please try again.")
    
    return a, b, c
  except ValueError:
    print('Invalid value. Please enter a three numeric values and seperate with spaces.')
    return None
a, b, c = get_quadratic_coefficients()
def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root_1 = (-b + (discriminant)**(1/2))/(2*a)
    root_2 = (-b - (discriminant)**(1/2))/(2*a)
    if discriminant > 0:
      print(f'There are two real distinct roots, {root_1} and {root_2}')
    elif discriminant == 0:
      print(f'There is one real repeated root, {root_1}')
    else:
      return None 
print(calculate_roots(a, b, c))