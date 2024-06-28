def linear_search(arr, gia_tri):
    for i in range(len(arr)):
        if arr[i] == gia_tri:
            return True
    return False

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gia_tri = 81

result = linear_search(arr, gia_tri)
if result:
    print(f"Giá trị {gia_tri} được tìm thấy trong danh sách.")
else:
    print(f"Giá trị {gia_tri} không có trong danh sách.")

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


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def search(root, key):
    if root is None or root.value == key:
        return root
    
    if root.value < key:
        return search(root.right, key)
    
    return search(root.left, key)

# Hàm để thêm một nút mới vào cây nhị phân
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
# Ví dụ sử dụng
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Tìm kiếm một giá trị trong cây
search_key = 40
result = search(root, search_key)
if result is not None:
    print(f"Giá trị {search_key} được tìm thấy trong cây nhị phân.")
else:
    print(f"Giá trị {search_key} không tồn tại trong cây nhị phân.")