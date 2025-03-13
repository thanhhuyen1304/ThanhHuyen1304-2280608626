def demSoLanXuatHien(value):
    count = {}
    for item in value:
        if item in count:
            count += 1
        else:
            count = 1
    return count
input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_string.split()
soLanXuatHien = demSoLanXuatHien(word_list)
print("Số lần xuất hiện của các phần tử: ", soLanXuatHien)