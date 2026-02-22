using { /Verse.org/Simulation }

#using { /Verse.org/Math }

math_solver := class():

    # Giải phương trình bậc 1: ax + b = 0
    SolveLinear(A : float, B : float) : void =
        if (not A = 0.0):
            Result := -B / A
            Print("PT Bac 1: x = {Result}")
        else if (B = 0.0):
            Print("PT Bac 1: Vo so nghiem")
        else:
            Print("PT Bac 1: Vo nghiem")

    # Giải phương trình bậc 2: ax^2 + bx + c = 0
    SolveQuadratic(A : float, B : float, C : float) : void =
        if (A = 0.0):
            SolveLinear(B, C)
        else:
            Delta := B * B - 4.0 * A * C
            
            if (Delta < 0.0):
                Print("PT Bac 2: Vo nghiem")
            else if (Delta = 0.0):
                X := -B / (2.0 * A)
                Print("PT Bac 2: Nghiem kep x = {X}")
            else:
                # Dung ham Sqrt tu thu vien Math
                if (SqrtDelta := Sqrt(Delta)):
                    X1 := (-B + SqrtDelta) / (2.0 * A)
                    X2 := (-B - SqrtDelta) / (2.0 * A)
                    Print("PT Bac 2: x1={X1}, x2={X2}")

    # Cac phep tinh co ban x, y
    CalculateBasic(X : float, Y : float) : void =
        Sum := X + Y
        Diff := X - Y
        Prod := X * Y
        Print("Tong: {Sum}, Hieu: {Diff}, Tich: {Prod}")
        
        # Kiem tra chia cho 0 bang context <decides>
        if (Div := X / Y?):
            Print("Thuong: {Div}")
        else:
            Print("Khong the chia cho 0")
    
    IntExam(X:int, Y:int) : int =
        X + Y

    # Flow thuc thi chinh
    RunCalculations() : void =
        CalculateBasic(10.0, 2.0)
        SolveLinear(2.0, -4.0)      # 2x - 4 = 0
        SolveQuadratic(1.0, -3.0, 2.0) # x^2 - 3x + 2 = 0