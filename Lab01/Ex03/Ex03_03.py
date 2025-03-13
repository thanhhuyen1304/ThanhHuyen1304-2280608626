def taoTuple(list):
    return tuple(list)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu cách: ")
value = list(map(int, input_list.split(' ')))
my_tuple = taoTuple(value)
print("List: ", value)
print("Tuple từ list: ", my_tuple)