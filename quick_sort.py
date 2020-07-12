def quick_sort(lista):

	iterator(lista, 0, len(lista)-1)
	
def iterator(lista, low, hi):

	if low < hi:
		p = partition(lista, low, hi)
		iterator(lista, low, p - 1)
		iterator(lista, p + 1, hi)
	
def get_pivot(lista, low, hi):
		
	mid = (hi + low) // 2
	s = sorted([lista[low], lista[mid], lista[hi]])
	if s[1] == lista[low]:
		return low
	elif s[1] == lista[mid]:
		return mid
	return hi
	
def partition(lista, low, hi):
	pivotIndex = get_pivot(lista, low, hi)
	pivotValue = lista[pivotIndex]
	lista[pivotIndex], lista[low] = lista[low], lista[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if lista[i] < pivotValue:
			border += 1
			lista[i], lista[border] = lista[border], lista[i]
	lista[low], lista[border] = lista[border], lista[low]

	return (border)
	
			
lista = [5,9,1,2,4,8,6,12,3,7]
print(lista)
quick_sort(lista)
print(lista)

