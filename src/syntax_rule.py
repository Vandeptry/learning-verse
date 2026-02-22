import re

KEYWORDS = [
    'using', 'device', 'creative_device', 'class', 'struct', 'enum', 'module',
    'void', 'int', 'float', 'string', 'logic', 'if', 'then', 'else', 'for', 
    'set', 'var', 'decides', 'suspends'
]

def check_syntax(code):
    errors = []
    lines = code.split('\n')
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for i, raw_line in enumerate(lines):
        line_num = i + 1
        line = raw_line.strip()
        if not line or line.startswith('#'): continue

        # 1. Kiểm tra cân bằng ngoặc
        for char in raw_line:
            if char in "([{": stack.append((char, line_num))
            elif char in ")]}":
                if not stack: errors.append(f"Lỗi dòng {line_num}: Thấy '{char}' nhưng không có dấu mở.")
                else:
                    top, _ = stack.pop()
                    if top != bracket_map[char]: errors.append(f"Lỗi dòng {line_num}: Sai kiểu ngoặc '{char}'.")

        # 2. Kiểm tra gán biến (:= hoặc : type =) - Fix lỗi False Positive
        if '=' in line and not any(k in line for k in ['if', 'using', 'set', 'return']):
            # Kiểm tra xem có dấu : đứng trước dấu = không (cho phép có chữ ở giữa)
            if not re.search(r':.*=', line) and ':=' not in line:
                errors.append(f"Lỗi dòng {line_num}: Thiếu ':' khi định nghĩa (Dùng ':=' hoặc ': type =').")

        # 3. Kiểm tra thiếu dấu : ở cuối các câu lệnh điều kiện/định nghĩa
        if any(line.startswith(k) for k in ['if', 'else', 'class', 'for', 'loop']):
            if not line.endswith(':'):
                errors.append(f"Lỗi dòng {line_num}: Thiếu dấu ':' để mở khối lệnh ở cuối dòng.")

    while stack:
        char, start_line = stack.pop()
        errors.append(f"Lỗi dòng {start_line}: Dấu '{char}' chưa đóng.")
    return errors