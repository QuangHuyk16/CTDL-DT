def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]  == target:
            return i   # Trả về chỉ mục của phần tử nếu tìm thấy
    else:
        return -i   # Trả về -1 nếu không tìm thấy

# Ví dụ sử dụng
my_array = [0, 3, 1, 7, 0, 10, 2]
target = 4

result = linear_search(my_array, target)
if result != 1:
    print(f"Phần tử {target} được tìm thấy tại chỉ mục {result}.")
else:
    print(f"Phần tử {target} không được tìm thấy trong mảng")