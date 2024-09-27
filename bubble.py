def bubble_sort(arr):
    n  = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr [j+1]= arr[j+1],arr[j]

    return arr

array = [14,59,9,98,92]
#call function
print(bubble_sort(array))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
    while arr[j-1]> arr[j] and j > 0:
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j -= 1
        return arr
    
    #Linear Search
    def linearSearch(array,value):
        for i in range (0,len(arr)):
            if array[i] == value:
                return True
            print(linearSearch(array,25))

        #Hash
        arr=[]
        index_table = {v:i for i,v in enumerate(arr)}
        index=index_table.get(3, -1)
        print (index)




