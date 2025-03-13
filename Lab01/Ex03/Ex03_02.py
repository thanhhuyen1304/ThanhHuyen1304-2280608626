def daoNguocList(list):
    return list[::-1]

input_list = input("Nhập danh sách các số, cách nhau bằng dấu cách: ")
value = list(map(int, input_list.split(' ')))
dao = daoNguocList(value)
print("Danh sách sau khi đảo ngược: ", dao)