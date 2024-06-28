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