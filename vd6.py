def partition(arr, low, high):
    i = low - 1
    pivot = arr[high] # Chọn pivot là phần tử cuối cùng của mảng
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high) # Chia mảng và lấy pivot
        quick_sort(arr, low, pi - 1) # Đệ qui sắp xếp nửa trái của pivot
        quick_sort(arr, pi + 1, high) # Đệ qui sắp xếp nửa phải của pivot
# Ví dụ sử dụng
my_array = [8, 3, 1, 7, 0, 10, 2]
quick_sort(my_array, 0, len(my_array) - 1)
print("Mảng đã được sắp xếp:", my_array)