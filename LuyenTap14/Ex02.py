names = []
for i in range(5):
    name = input(f"Nhập tên người thứ {i+1}: ")
    names.append(name)
print("Danh sách ban đầu:", names)

if len(names) >= 2:
    names.pop(1)

print("Danh sách sau khi xóa:", names)
