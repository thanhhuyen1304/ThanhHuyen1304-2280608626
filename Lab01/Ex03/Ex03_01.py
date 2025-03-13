def tinhTongChan(list):
    tong = 0
    for i in list:
        if i % 2 ==0:
            tong += i
    return tong
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
value = list(map(int, input_list.split(',')))
tongChan = tinhTongChan(value)
print("Tổng các số chẵn trong danh sách là: ", tongChan)