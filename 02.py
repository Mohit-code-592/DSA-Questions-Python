#search element in a array
def search_element(my_list,taget):
    index = -1
    for i in range(len(my_list)):
        if my_list[i] == taget:
            index = i
            break
    
    return index

my_list = [1,2,3,52,22,6,8]
taget = int(input("Enter taget value : "))
index_num = search_element(my_list,taget)

print(f"index value is : {index_num}")
      
       
    
