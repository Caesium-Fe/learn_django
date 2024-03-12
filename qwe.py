import os
import re


def path_check(path):
    if re.match(".*[DV]\\d\\d.*", os.path.basename(path)):
        return True
    else:
        return False


def file_check(path):
    if re.match(".*[DV]\\d\\d.*.(csv|xlsx)", os.path.basename(path)):
        return True
    else:
        return False


def file_dfs(path: str):
    """
    刷出文件夹内所有DXX文件
    """
    if os.path.isfile(path):
        if file_check(path):
            print(path)
            return

    if os.path.isdir(path):
        if path_check(path):
            print(path)

        try:
            listdir = os.listdir(path)
        except Exception:
            return
        for a in listdir:
            file_dfs(path + os.sep + a)


if __name__ == '__main__':
    file_dfs("F:\\")