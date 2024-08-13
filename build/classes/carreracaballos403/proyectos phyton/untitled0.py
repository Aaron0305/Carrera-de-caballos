import math

def golden_section_maximization(func, XL, XR, tol=1e-6):
    gr = (math.sqrt(5) - 1) / 2  # Ratio de la sección dorada
    x1 = XR - gr * (XR - XL)
    x2 = XL + gr * (XR - XL)
    iterations = 0

    while (XR - XL) > tol:
        iterations += 1
        if func(x1) > func(x2):
            XR = x2
        else:
            XL = x1

        x1 = XR - gr * (XR - XL)
        x2 = XL + gr * (XR - XL)

      

        if 0 <= x1 <= 2:
            print(f'F(x) = {3 * x1}')
        elif 2 <= x1 <= 3:
            print(f'F(g) = {1 / 3 * (-x2 + 20)}')
        else:
            print("Outside defined range")

        print(f"Iteración {iterations-1}: x1 = {x1}, x2 = {x2}")

    maximum = (XL + XR) / 2
    max_value = func(maximum)

    return maximum, max_value

# Function example (you can replace it)
def example_function(x):
    return -(x - 2) ** 2  # Negative to find the maximum

# Ask the user for input
XL = float(input("Introduce XL (límite inferior del intervalo): "))
XR = float(input("Introduce XR (límite superior del intervalo): "))
tol = float(input("Introduce la tolerancia: "))

max_x, max_value = golden_section_maximization(example_function, XL, XR, tol)
exactitud = XR - XL

print(f"Maximo encontrado en x = {max_x}")
print(f"Nivel de exactitud: {exactitud}")
print(f"Intervalo resultante: [{XL}, {XR}]")