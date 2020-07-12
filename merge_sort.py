import sys

def merge_sort(lista):
	iterator(lista, 0, len(lista)-1)
	
def iterator(lista, inicio, fim):
	if inicio < fim:
		meio = (inicio + fim)//2
		iterator(lista, inicio, meio)
		iterator(lista, meio+1, fim)
		merge(lista, inicio, meio, fim)
		
def merge(lista, inicio, meio, fim):

	L = lista[inicio:meio+1]
	R = lista[meio+1:fim+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	k = j = 0
	
	for i in range (inicio, fim+1):
		if L[k] <= R[j]:
			lista[i] = L[k]
			k += 1
			
		else:
			lista[i] = R[j]
			j += 1
		print(lista)
TESTE = [9,6,2,3,7,9,2,0,4,11]
print(TESTE)
merge_sort(TESTE)
print(TESTE)