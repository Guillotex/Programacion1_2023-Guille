def promedio(arreglo):
  suma = 0
  contador = 0
  for a in arreglo:
    suma += float(a)
  prome = suma / contador
  print(prome)
  return promedio