array = [3, 7, 1]

def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

bubblesort(array)