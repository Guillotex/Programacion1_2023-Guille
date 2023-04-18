# Hola mundo 
print("Hola guille")

# Consultar tipo de dato 
print(type("hola guille"))  # Tipo "string"    
print(type(5))     # Tipo "int" 
print(type(6.4))     # Tipo "float" 
print(type(3 + 1j))   # Tipo "complex" 
print(type(False))    # Tipo "bool" 


def promedio(arreglo):
  suma = 0
  contador = 0
  for a in arreglo:
    suma += float(a)
    contador += 1
  promed = suma / contador
  print(promed)
  return promedio
