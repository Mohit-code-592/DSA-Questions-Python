#rotate element in array by 1

def rotate_element(arr):
    store = arr[len(arr) - 1]
    
    for i in range(len(arr) - 2 , -1 , -1):
        arr[i + 1] = arr[i]
    
    arr[0] = store


arr = [1,2,3,4,6]
rotate_element(arr)
print(arr)
