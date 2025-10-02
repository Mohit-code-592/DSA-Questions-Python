#fibonacci series in array

def fibonacci(arr,element):
    first = arr[0]
    second = arr[1]

    if element == 1:
        return 0
    elif element == 2:
        return 1
    
    for i in range(2,element):
        third = first + second
        arr.append(third)
        first = second
        second = third

    return arr[element-1]
    
arr = [0,1]
element = int(input("Enter element : "))

result = fibonacci(arr,element)
print(result)
print(arr)
