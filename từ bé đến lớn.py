nb = [8, 3, 1, 5, 2, 9, 4, 6, 7]
# arr.sort(reverse=True)
# print(arr)

for a in range(0,len(nb)):
    for t in range(a+1,len(nb)):
        if nb[t]<nb[a]:
            temp = nb[a]
            nb[a]=nb[t]
            nb[t]=temp
print(nb)            


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ví dụ thuật toán sắp xếp chọn
if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print("Danh sách ban đầu: ", arr)
    selection_sort(arr)
    print("Danh sách sau khi sắp xếp: ", arr)               



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 

# Ví dụ sử dụng
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print("Mảng đã sắp xếp là: ")
    for i in range(len(arr)):
        print(arr[i])          


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