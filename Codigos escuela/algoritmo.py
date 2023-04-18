import math

#Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C
#respectivamente. El algoritmo debe imprimir cual es el mayor y cual es el menor. Recuerde constatar que
#los tres valores introducidos por el teclado sean valores distintos. Presente un mensaje de alerta en caso de
#que se detecte la introducción de valores iguales.

valor_a = int(input("introduzca el valor a"))
valor_b = int(input("introduzca el valor b"))
valor_c = int(input("introduzca el valor c"))

lista_de_valores = [valor_a, valor_b, valor_c]





numeros = []


for i in range(3):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)


mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("Mayor:", mayor)



#Determinar la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos.
#Desarrolle el algoritmo correspondiente

cateto_a = 10
cateto_b = 20

h = math.sqrt((cateto_a* 2) + (cateto_b * 2))


#Desarrolle un algoritmo que permita determinar el área y volumen de un cilindro dado su radio (R) y
#altura (H).

valor_radio = int(input("introduzca el radio: "))

valor_altura = int(input("introduzca la altura: "))

pi = 3.14

volumenCilindro = pi * (valor_radio * 2 ) * valor_altura

area = 2 * pi * valor_radio * valor_altura


print ("Volúmne: " + str(volumenCilindro))
print ("Area: " + str(area))




#Desarrolle un algoritmo que permita leer un valor cualquiera N y escriba si dicho número es par o impar.

numero = 0

numero = int(input("Indique un número: "))
residuo = math.fmod(numero,2)
          
if (residuo == 0):
    print(numero, " es par")
if (residuo == 1):
    print(numero, " es impar" )











