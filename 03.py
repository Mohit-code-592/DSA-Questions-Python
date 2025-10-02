#reverse a array

#we also have built in method for reverse

#first method
def reverse_array(my_list):
    arr = []
    for i in range(len(my_list) - 1 , -1 ,-1):
        arr.append(my_list[i])
    return arr

#second and efficent method

def rev_arr(my_list):
    first_index = 0
    last_index = len(my_list) - 1

    while first_index < last_index:
        my_list[first_index] , my_list[last_index] = my_list[last_index] , my_list[first_index]

        first_index += 1
        last_index -= 1




my_list = [1,2,3,4,5]
# new_arr = reverse_array(my_list)

# print(new_arr)

rev_arr(my_list)
print(my_list)

