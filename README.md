# Nhập dữ liệu cho bài toán phát hiện Deadlock

Chương trình Python đơn giản dùng để **nhập và kiểm tra dữ liệu đầu vào** cho bài toán phát hiện bế tắc (deadlock) trong hệ điều hành. Dữ liệu gồm hai ma trận **Allocation**, **Request** và vector **Available**.

Tệp chính: `nhap_du_lieu_don_gian.py`

## Tính năng

- Nhập số lượng tiến trình `n` và số loại tài nguyên `m`.
- Nhập ma trận **Allocation** (n × m), ma trận **Request** (n × m) và vector **Available** (m phần tử).
- Kiểm tra dữ liệu ngay khi nhập. Nhập sai thì báo lỗi và hỏi lại.
- Tính tổng tài nguyên của hệ thống (**Total**) và đưa ra cảnh báo nếu có tiến trình xin nhiều hơn tổng tài nguyên.
- In lại toàn bộ dữ liệu để người dùng kiểm tra bằng mắt.

## Yêu cầu

- Python 3.6 trở lên.
- Không cần cài thêm thư viện nào.

## Ý nghĩa dữ liệu

Hệ thống có `n` tiến trình (P0, P1, …) và `m` loại tài nguyên (R0, R1, …). Mỗi loại tài nguyên có thể có nhiều đơn vị giống nhau.

| Tên | Kích thước | Ý nghĩa |
|---|---|---|
| **Allocation** | n × m | `Allocation[i][j]` là số đơn vị Rj mà Pi **đang giữ** |
| **Request** | n × m | `Request[i][j]` là số đơn vị Rj mà Pi **đang chờ được cấp** |
| **Available** | m | `Available[j]` là số đơn vị Rj **đang rảnh** |

Tổng tài nguyên của hệ thống được tính bằng:

```
Total[j] = (tổng cột j của Allocation) + Available[j]
```

## Cách nhập dữ liệu

- Mỗi **hàng** của ma trận nhập trên **một dòng**, các số cách nhau bằng dấu cách. Ví dụ: `0 1 0`.
- Hàng thứ i ứng với tiến trình Pi.
- Số lượng giá trị trên một dòng phải đúng bằng `m`.

## Các lỗi chương trình kiểm tra

| Tình huống | Thông báo |
|---|---|
| `n`, `m` không phải số nguyên | `Lỗi: bạn phải nhập một số nguyên.` |
| `n`, `m` nhỏ hơn 1 | `Lỗi: số phải lớn hơn hoặc bằng 1` |
| Nhập thiếu hoặc thừa số trên một dòng | `Lỗi: cần đúng 3 số, bạn nhập 2 số.` |
| Có giá trị không phải số nguyên | `Lỗi: x không phải số nguyên.` |
| Có giá trị âm | `Lỗi: không được nhập số âm ( -1 )` |

**Cảnh báo** (dữ liệu vẫn hợp lệ nhưng đáng chú ý): khi `Request[i][j]` lớn hơn `Total[j]`, tiến trình đó sẽ không bao giờ được thỏa mãn.

## Ví dụ chạy

Dữ liệu mẫu gồm 5 tiến trình và 3 loại tài nguyên:

```
=== NHẬP DỮ LIỆU PHÁT HIỆN DEADLOCK ===
Nhập số tiến trình (n): 5
Nhập số loại tài nguyên (m): 3

Nhập ma trận Allocation ( 5 hàng x 3 cột )
  Allocation của P0: 0 1 0
  Allocation của P1: 2 0 0
  Allocation của P2: 3 0 3
  Allocation của P3: 2 1 1
  Allocation của P4: 0 0 2

Nhập ma trận Request ( 5 hàng x 3 cột )
  Request của P0: 0 0 0
  Request của P1: 2 0 2
  Request của P2: 0 0 1
  Request của P3: 0 0 0
  Request của P4: 0 0 0

Nhập vector Available ( 3 số )
  Available: 0 0 0

=== DỮ LIỆU ĐÃ NHẬP ===
n = 5 , m = 3

Allocation:
  P0 [0, 1, 0]
  P1 [2, 0, 0]
  P2 [3, 0, 3]
  P3 [2, 1, 1]
  P4 [0, 0, 2]

Request:
  P0 [0, 0, 0]
  P1 [2, 0, 2]
  P2 [0, 0, 1]
  P3 [0, 0, 0]
  P4 [0, 0, 0]

Available: [0, 0, 0]

Tổng tài nguyên của hệ thống (Total): [7, 2, 6]
Không có cảnh báo nào.

=> Dữ liệu hợp lệ.
```

## Cấu trúc chương trình

| Hàm | Chức năng |
|---|---|
| `nhap_so_nguyen(cau_hoi, nho_nhat)` | Nhập một số nguyên (dùng cho `n` và `m`) |
| `nhap_mot_dong(cau_hoi, so_phan_tu)` | Nhập một dòng gồm nhiều số nguyên không âm |
| `nhap_ma_tran(ten, so_hang, so_cot)` | Nhập cả ma trận bằng cách nhập từng dòng |
| `in_ma_tran(ten, ma_tran)` | In ma trận ra màn hình |
| `kiem_tra_canh_bao(...)` | Tính Total và đưa ra cảnh báo |
| `main()` | Chạy toàn bộ chương trình |

## Hướng phát triển

- Thêm thuật toán tìm dãy tiến trình hợp lệ để kết luận hệ thống có deadlock hay không và tiến trình nào bị deadlock.
- Đọc dữ liệu từ tệp thay vì nhập tay.
