#cai nay la use client
   
print("\n=== Client Data Menu ===")
MSSV = input('Nhập ID khách hàng: ').upper()


ID = f"{MSSV}.txt"

try:
            # Mở file nếu tồn tại
    with open(ID, 'r', encoding="utf-8") as f:
        data = f.read()
    print("\nThông tin khách hàng hiện tại:")
    print(data)

except FileNotFoundError:
    print(f"\nKhông tìm thấy file: {ID}")
    client_name = input('Nhập tên người dùng mới: ').strip()
    with open(ID, 'w', encoding="utf-8") as f:
        f.write(f"ID: {MSSV}\n")
        f.write(f"Tên: {client_name}\n")
        f.write("Sách đã mượn: (chưa có)\n")
        f.write("Số ngày còn lại để trả: 0\n")
    print(f"\nĐã tạo hồ sơ mới cho khách hàng {client_name} (ID: {MSSV})")
    print("Sách đã mượn: (chưa có)")
    print("Số ngày còn lại để trả: 0")

input("\nNhấn Enter để quay lại menu người dùng...")
    

