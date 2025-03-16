def count_lines(file_name):
    txt = open(f"{file_name}", "r", encoding="utf-8")
    lines = txt.readlines()
    txt.close()
    return len(lines)


print(count_lines(r"C:\Users\user\Desktop\PP2\lab6\dir_and_files\text.txt"))