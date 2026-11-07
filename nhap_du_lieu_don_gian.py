# -*- coding: utf-8 -*-
"""
NHẬP DỮ LIỆU CHO BÀI TOÁN PHÁT HIỆN DEADLOCK (bản đơn giản)

Chương trình hỏi người dùng:
  1. n  = số tiến trình
  2. m  = số loại tài nguyên
  3. Allocation = ma trận n x m (tiến trình đang GIỮ bao nhiêu)
  4. Request    = ma trận n x m (tiến trình đang CHỜ bao nhiêu)
  5. Available  = vector m phần tử (tài nguyên đang RẢNH)

Nhập sai thì chương trình báo lỗi và hỏi lại.
"""


# ---------------------------------------------------------
# HÀM 1: Nhập một số nguyên (dùng cho n và m)
# ---------------------------------------------------------
def nhap_so_nguyen(cau_hoi, nho_nhat):
    while True:                              # lặp mãi cho đến khi nhập đúng
        try:
            so = int(input(cau_hoi))         # thử đổi chữ thành số nguyên
        except ValueError:                   # nếu không đổi được thì vào đây
            print("Lỗi: bạn phải nhập một số nguyên.")
            continue                         # quay lại đầu vòng lặp, hỏi lại

        if so < nho_nhat:
            print("Lỗi: số phải lớn hơn hoặc bằng", nho_nhat)
            continue

        return so                            # nhập đúng thì trả kết quả


# ---------------------------------------------------------
# HÀM 2: Nhập một dòng gồm nhiều số (dùng cho 1 hàng của ma trận)
# ---------------------------------------------------------
def nhap_mot_dong(cau_hoi, so_phan_tu):
    while True:
        text = input(cau_hoi)                # ví dụ người dùng gõ: "0 1 0"
        cac_phan_tu = text.split()           # tách thành danh sách: ["0", "1", "0"]

        # Kiểm tra 1: đủ số phần tử chưa?
        if len(cac_phan_tu) != so_phan_tu:
            print("Lỗi: cần đúng", so_phan_tu, "số, bạn nhập", len(cac_phan_tu), "số.")
            continue

        # Kiểm tra 2 và 3: từng phần tử có phải số nguyên không âm không?
        dong = []                            # danh sách rỗng, sẽ chứa các số
        hop_le = True                        # giả sử ban đầu là đúng

        for chu in cac_phan_tu:
            try:
                so = int(chu)
            except ValueError:
                print("Lỗi:", chu, "không phải số nguyên.")
                hop_le = False
                break                        # dừng kiểm tra dòng này

            if so < 0:
                print("Lỗi: không được nhập số âm (", so, ")")
                hop_le = False
                break

            dong.append(so)                  # số đúng thì thêm vào danh sách

        if hop_le:
            return dong                      # cả dòng đúng thì trả về


# ---------------------------------------------------------
# HÀM 3: Nhập ma trận (gồm nhiều dòng)
# ---------------------------------------------------------
def nhap_ma_tran(ten, so_hang, so_cot):
    print()
    print("Nhập ma trận", ten, "(", so_hang, "hàng x", so_cot, "cột )")
    ma_tran = []                             # ma trận là danh sách các dòng
    for i in range(so_hang):                 # i chạy 0, 1, 2, ... so_hang-1
        dong = nhap_mot_dong("  " + ten + " của P" + str(i) + ": ", so_cot)
        ma_tran.append(dong)
    return ma_tran


# ---------------------------------------------------------
# HÀM 4: In ma trận ra màn hình cho dễ nhìn
# ---------------------------------------------------------
def in_ma_tran(ten, ma_tran):
    print()
    print(ten + ":")
    for i in range(len(ma_tran)):
        print("  P" + str(i), ma_tran[i])


# ---------------------------------------------------------
# HÀM 5: Kiểm tra cảnh báo (dữ liệu đúng nhưng đáng chú ý)
# ---------------------------------------------------------
def kiem_tra_canh_bao(n, m, allocation, request, available):
    # Tổng tài nguyên mỗi loại = tổng cột của Allocation + Available
    tong = []
    for j in range(m):                       # duyệt từng loại tài nguyên
        cong = available[j]
        for i in range(n):                   # cộng số đang giữ của từng tiến trình
            cong = cong + allocation[i][j]
        tong.append(cong)

    print()
    print("Tổng tài nguyên của hệ thống (Total):", tong)

    # Cảnh báo nếu một tiến trình xin nhiều hơn tổng của hệ thống
    co_canh_bao = False
    for i in range(n):
        for j in range(m):
            if request[i][j] > tong[j]:
                print("Cảnh báo: P" + str(i), "xin", request[i][j], "đơn vị R" + str(j),
                      "nhưng cả hệ thống chỉ có", tong[j])
                co_canh_bao = True

    if not co_canh_bao:
        print("Không có cảnh báo nào.")


# ---------------------------------------------------------
# CHƯƠNG TRÌNH CHÍNH
# ---------------------------------------------------------
def main():
    print("=== NHẬP DỮ LIỆU PHÁT HIỆN DEADLOCK ===")

    n = nhap_so_nguyen("Nhập số tiến trình (n): ", 1)
    m = nhap_so_nguyen("Nhập số loại tài nguyên (m): ", 1)

    allocation = nhap_ma_tran("Allocation", n, m)
    request = nhap_ma_tran("Request", n, m)

    print()
    print("Nhập vector Available (", m, "số )")
    available = nhap_mot_dong("  Available: ", m)

    # Hiển thị lại dữ liệu để người dùng kiểm tra bằng mắt
    print()
    print("=== DỮ LIỆU ĐÃ NHẬP ===")
    print("n =", n, ", m =", m)
    in_ma_tran("Allocation", allocation)
    in_ma_tran("Request", request)
    print()
    print("Available:", available)

    kiem_tra_canh_bao(n, m, allocation, request, available)
    print()
    print("=> Dữ liệu hợp lệ.")


main()
