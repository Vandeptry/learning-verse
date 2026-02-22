using { /Verse.org/Simulation }
using { /Verse.org/Debugging }

# Định nghĩa một class đơn giản
devops_manager := classs():
    # Thuộc tính hằng số
    MaxRetries : int = 3
    
    # Hàm kiểm tra trạng thái (có thể thất bại)
    CheckServerStatus<public>(Uptime : int)<decides> : void =
        Uptime > 0 # Nếu điều kiện này sai, toàn bộ hàm sẽ "Fail"
        Print("Server is Healthy")

    CheckServerStatus[Uptime : int] : void =
        if (Uptime <= 0):
            Print("Server is Down")

    CheckServerBandwitch<private>(x : int):void =
        if(x < 100):
            Print("Low bw")
        else if (x>600)
            Print("High bw")        
        else
            Print("Normal bw")
    # Hàm thực thi chính
    RunMaintenance() : void =
        # Thử gọi hàm có khả năng fail trong một context cho phép fail (if)
        if (CheckServerStatus[100]):
            Print("Maintenance unnecessary")