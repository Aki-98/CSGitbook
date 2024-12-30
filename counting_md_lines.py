import os


def count_md_lines(directory):
    """计算指定文件夹及其子文件夹中所有 .md 文件的总行数"""
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        line_count = sum(1 for line in f)
                        total_lines += line_count
                        print(f"{file_path}: {line_count} lines")
                except Exception as e:
                    print(f"无法读取文件 {file_path}，原因：{e}")
    print(f"\n总行数: {total_lines}")
    return total_lines


# 使用方法
if __name__ == "__main__":
    folder_path = input("请输入文件夹路径: ").strip()
    if os.path.isdir(folder_path):
        count_md_lines(folder_path)
    else:
        print("无效的文件夹路径")
