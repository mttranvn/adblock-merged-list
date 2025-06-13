import os

def main():
    input_file = "merged.txt"

    lines = set()

    if os.path.exists(input_file):
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    lines.add(line)

    sorted_lines = sorted(lines)

    # Ghi lại vào merged.txt
    with open(input_file, "w", encoding="utf-8") as f:
        for line in sorted_lines:
            f.write(line + "\n")

    # Cập nhật README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Adblock Merged List\n\n")
        f.write(f"- Số dòng hiện tại: **{len(sorted_lines)}**\n")
        f.write(f"- Cập nhật tự động bằng GitHub Actions.\n")

if __name__ == "__main__":
    main()
