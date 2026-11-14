
from pathlib import Path
from datetime import datetime
import os
import re
import shutil

# 当前脚本所在目录
SCRIPT_DIR = Path(__file__).resolve().parent

# 图片标记文件
MARKER = "dkx_img1.txt"

# Markdown 图片路径
PATTERN = re.compile(
    r'(!\[[^\]]*\]\()(<[^>]+>|[^)\s]+)([^)]*\))'
)


def find_img():
    """向上查找标记文件，确定 img 目录"""

    for folder in [SCRIPT_DIR, *SCRIPT_DIR.parents]:
        if (folder / MARKER).is_file():
            img_dir = folder / "img"

            if img_dir.is_dir():
                return img_dir

            raise FileNotFoundError("标记文件所在目录没有 img 文件夹")

    raise FileNotFoundError(f"找不到 {MARKER}")


def main():
    print("=" * 45)
    print("       Hexo 图片路径自动修复工具")
    print("=" * 45)

    img_dir = find_img()

    print(f"\n图片目录：{img_dir}")
    print(f"文章目录：{SCRIPT_DIR}")

    name = input("\n请输入文章名称：").strip().strip('"')

    if not name.lower().endswith(".md"):
        name += ".md"

    md_file = SCRIPT_DIR / name

    if not md_file.is_file():
        print("错误：找不到指定文章！")
        return

    content = md_file.read_text(encoding="utf-8-sig")
    count = 0

    def replace(match):
        nonlocal count

        prefix, raw_path, suffix = match.groups()

        wrapped = raw_path.startswith("<") and raw_path.endswith(">")
        path = raw_path[1:-1] if wrapped else raw_path

        # 跳过网络图片
        if path.startswith(("http://", "https://", "//", "data:")):
            return match.group(0)

        # 分离参数和锚点
        path_part = re.split(r"[?#]", path, maxsplit=1)[0]
        extra = path[len(path_part):]

        # 统一路径分隔符
        parts = path_part.replace("\\", "/").split("/")

        # 找到 img 目录标识
        if "img" not in parts:
            return match.group(0)

        index = parts.index("img")

        # 保留 img 后面的所有路径
        remaining = parts[index + 1:]

        if not remaining:
            return match.group(0)

        # 计算文章目录到 img 目录的相对路径
        new_path = Path(os.path.relpath(
            img_dir, SCRIPT_DIR
        )).as_posix()

        new_path += "/" + "/".join(remaining) + extra

        if wrapped or " " in new_path:
            new_path = f"<{new_path}>"

        if new_path != raw_path:
            count += 1
            print(f"\n原路径：{raw_path}")
            print(f"新路径：{new_path}")

        return prefix + new_path + suffix

    new_content = PATTERN.sub(replace, content)

    if count == 0:
        print("\n没有需要修改的图片路径。")
        return

    confirm = input(f"\n发现 {count} 处路径需要修复，确认修改？(Y/N)：")

    if confirm.strip().lower() != "y":
        print("已取消修改。")
        return

    # 自动备份
    backup = md_file.with_name(
        md_file.name + ".backup_" +
        datetime.now().strftime("%Y%m%d_%H%M%S")
    )

    shutil.copy2(md_file, backup)

    # 保存修复结果
    md_file.write_text(new_content, encoding="utf-8")

    print("\n修复成功！")
    print(f"修改数量：{count}")
    print(f"备份文件：{backup.name}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n错误：{e}")

    input("\n按回车退出...")
