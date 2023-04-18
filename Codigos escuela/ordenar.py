def mostrar_lista(lista): 
 linea = ""   
 for valor in lista: 
    linea = linea + " " + str(valor)
 print(linea)    

def ordenar_menor(lista): 
   long= len(lista)
   l=long

  # mostrar_lista(lista,long)

   n = -1
   while(n !=0 ):
      n = 0
      for indice in range(1,l,1):
            if lista[indice-1]>lista[indice]:   #Para hacer que sea de mayor a menor cambiar el signo " < " 
               temp=lista[indice - 1]
               lista[indice-1]=lista[indice]
               lista[indice]=temp
               n=indice
               #mostrar_lista(lista,long)
      l = n
   return lista 

def ordenar_mayor(lista):
   long= len(lista)
   l=long

   #mostrar_lista(lista,long)

   n = -1
   while(n !=0 ):
      n = 0
      for indice in range(1,l,1):
            if lista[indice-1]<lista[indice]:   #Para hacer que sea de mayor a menor cambiar el signo " < " 
               temp=lista[indice - 1]
               lista[indice-1]=lista[indice]
               lista[indice]=temp
               n=indice
               #mostrar_lista(lista,long)
      l = n
   return lista   

#lista = [9,8,7,3,10,3.5]
lista = ["casi","zorro","auto","case","casa"]

print("lista original")
mostrar_lista(lista)
print("lista ordenada decendentemente")
mostrar_lista(ordenar_menor(lista))
print("lista ordenada ascendentemente")
mostrar_lista(ordenar_mayor(lista))