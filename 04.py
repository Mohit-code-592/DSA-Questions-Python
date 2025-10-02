#find the second max-element in array

def second_max(my_list):
    max_element = my_list[0]
    pre_max = -1

    if len(my_list) < 2:
        return pre_max

    
    for i in range(1,len(my_list)):
        if max_element < my_list[i]:
            pre_max = max_element
            max_element = my_list[i]
    
        elif my_list[i] > pre_max and my_list[i] != max_element:
            pre_max = my_list[i]
    
    return pre_max

my_list = [1,7,9,0,2,3,5,6]

second_max_element = second_max(my_list)

print(f"second max element is {second_max_element}")

