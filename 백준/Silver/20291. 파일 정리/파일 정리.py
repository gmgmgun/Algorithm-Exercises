cnt = int(input())
strings = [input() for _ in range(cnt)]


def organize_files(files):
    ext_dict = {}

    for file in files:
        _, ext = file.split('.')
        if ext in ext_dict:
            ext_dict[ext] += 1
        else:
            ext_dict[ext] = 1

    for ext in sorted(ext_dict):
        print(f"{ext} {ext_dict[ext]}")


organize_files(strings)