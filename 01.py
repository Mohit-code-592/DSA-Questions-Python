#find the min and max value
def min_max_element(my_list):
    min_value = my_list[0]
    max_value = my_list[0]

    for i in range(1,len(my_list)):
        if min_value > my_list[i]:
            min_value = my_list[i]
            
        elif max_value < my_list[i]:
            max_value = my_list[i]

    
    return min_value,max_value

my_list = [11,22,33,44,1,5,0,12]

min_value,max_value = min_max_element(my_list)

print(f"Max element in array is : {max_value}")

print(f"Min element in array is : {min_value}")




