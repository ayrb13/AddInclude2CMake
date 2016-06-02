"""
为clion的CMakeLists.txt增加include路径

将该脚本置于clion项目根目录,与CMakeLists.txt同目录
执行该脚本即可自动添加include路径
"""

import os

ret = []
def SolveDirectory():
    for rt, dirs, files in os.walk("."):
        needInclude = False
        for i in files:
            if i[-2:] == ".h":
                needInclude = True
                break
        if rt.find("include") != -1:
            needInclude = True
        if needInclude:
            ret.append("include_directories(" + rt + ")")

if __name__ == "__main__":
    f = open('CMakeLists.txt', 'a')
    f.write("\n\n#add by AddInclude2Clion.py\n")
    SolveDirectory()
    for i in ret:
        f.write(i + "\n")
