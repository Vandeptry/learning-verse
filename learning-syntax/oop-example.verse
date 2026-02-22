using { /Verse.org/Simulation }

# Một class mô phỏng máy tính
calculator := class():
    # Thuộc tính có thể thay đổi (var)
    var LastResult : float = 0.0

    # Hàm trả về giá trị (float), không dùng return
    Add(X:float, Y:float) : float = 
        X + Y

    # Hàm public, có khả năng thất bại (decides)
    Divide<public>(X:float, Y:float)<decides> : float =
        not Y = 0.0  # Nếu Y = 0, hàm sẽ "Fail" ngay tại đây
        X / Y        # Nếu không fail, trả về thương số

    # Flow thực thi
    Run() : void =
        A := 10.0
        B := 5.0
        # Gọi hàm trả về giá trị và gán vào chuỗi
        Sum := Add(A, B)
        Print("Tong cua {A} va {B} la: {Sum}")

        # Xử lý hàm có thể fail bằng 'if'
        if (Result := Divide[A, B]):
            set LastResult = Result
            Print("Chia thanh cong: {Result}")
        else:
            Print("Loi: Khong the chia cho 0")