import os
import sys
import re
from syntax_rule import check_syntax

class VerseEmulator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.code = ""

    def compile_virtual(self):
        print(f"--- Đang kiểm tra: {self.file_path} ---")
        if not os.path.exists(self.file_path):
            print(f"Lỗi: Không tìm thấy file tại {self.file_path}")
            return False

        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.code = f.read()

        errors = check_syntax(self.code)
        if errors:
            for err in errors: print(f"[SYNTAX ERROR] {err}")
            return False
        
        print("[SUCCESS] Cú pháp hợp lệ.")
        if not os.path.exists('build'): os.makedirs('build')
        with open('build/output.vsc', 'w') as f:
            f.write(f"Compiled_Data_of_{os.path.basename(self.file_path)}")
        return True

    def run_mock(self):
        print("--- Thực thi logic (Giả lập) ---")
        prints = re.findall(r'Print\s*\(\s*"(.*?)"\s*\)', self.code)
        if prints:
            for text in prints:
                print(f"Verse_Output: {text}")
        else:
            print("Log: Device chạy nhưng không có lệnh Print nào được thực hiện.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_verse_files():
    search_dirs = ['src', 'learning-syntax']
    verse_files = []
    for d in search_dirs:
        if os.path.exists(d):
            verse_files.extend([os.path.join(d, f) for f in os.listdir(d) if f.endswith('.verse')])
    return verse_files

if __name__ == "__main__":
    clear_screen()
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Nếu không tham số, hiển thị menu chọn file
        files = get_verse_files()
        if not files:
            print("Không tìm thấy file .verse nào trong 'src' hoặc 'learning-syntax'.")
            sys.exit()
            
        print("=== VERSE EMULATOR MENU ===")
        for i, f in enumerate(files, 1):
            print(f"{i}. {f}")
        
        try:
            choice = input(f"\nChọn file (1-{len(files)}) hoặc Enter để chạy file đầu tiên: ")
            index = int(choice) - 1 if choice.strip() else 0
            target = files[index] if 0 <= index < len(files) else files[0]
            clear_screen()
        except (ValueError, IndexError):
            target = files[0]

    emulator = VerseEmulator(target)
    if emulator.compile_virtual():
        emulator.run_mock()