# Encontrando números primos
# Los números primos entre 1 y n
# Por: Santiago, L. D.

def main():
	n=eval(input("Ingresa el rango n= ")) # Pedimos el máximo
	a=[2] # Inicializamos la lista donde guardaremos los primos que encontremos
	enarchivo = open("Estos_son_primos.txt","w")

	#print("\n",a[0], end="\n") # Imprimimos el 2 primero
	print(a[0], end="\n", file=enarchivo) # Imprimimos el 2 primero

	for i in range(3,n+1,2): # Comenzamos a comparar a i desde 3, revisando solo números nones: 3,5,7,9,11...
		L=len(a)
		for j in range(L): # Probaremos la divisivilidad de i por los primos ya encontrados guardados en a
			if a[j] > (i//2)+1: # No tiene sentido seguir comparando con primos mayores a i/2
				break

			if i%a[j] == 0: # Comparando divisibilidad
				z=1 # con un divisor que encontremos, i no es primo
				break
			elif i%a[j] != 0:
				z=0


		if z == 0: # Será número primo si z es cero
	#		print(i,end="\n") # Imprimimos y
			print(i,end="\n", file=enarchivo)
			a.append(i) # agregamos a lista el nuevo primo





main()
