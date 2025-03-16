import os

RED = "\033[91m"
RESET = "\033[0m"

def search(dirname):
    count = 0   # .py 파일 개수 저장 변수

    try:
        if not os.path.exists(dirname):
            print(f"{RED}경로 없음: {dirname}{RESET}")
            return 0

        with os.scandir(dirname) as entries:
            for entry in entries:
                full_filename = entry.path
                if entry.is_dir():
                    count += search(full_filename)
                elif entry.is_file() and entry.name.endswith('.py'):
                    print(full_filename)
                    count += 1

        # filenames = os.listdir(dirname)
        # for filename in filenames:
        #     full_filename = os.path.join(dirname, filename)
        #     if os.path.isdir(full_filename):
        #         search(full_filename)
        #     else:
        #         ext = os.path.splitext(full_filename)[-1]
        #         if ext == '.py':
        #             print(full_filename)
    except PermissionError as e:
        print(f"{RED}PermissionError: {e}{RESET}")
    except FileNotFoundError as e:
        print(f"{RED}FileNotFoundError: {e}{RESET}")

    return count

count = search("c:/")
print(f"\n총 *.py 파일 개수:", count)