def truyCapPhanTu(num):
    first_value = num[0]
    last_value = num[-1]
    return first_value, last_value

input_tuple = input("Nhập tuple, ví dụ (1, 2, 3): ")
first, last = truyCapPhanTu(input_tuple)
print("Phần tử đầu tiên: ", first)
print("Phần tử cuối cùng: ", last)