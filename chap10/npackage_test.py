"""导入命名空间包"""

import sys
sys.path.append('dir1')  # 添加文件夹“dir1”到搜索路径
sys.path.append('dir2')  # 添加文件夹“dir2”到搜索路径

import npack.abc         # “dir1\npack\abc.py”导入模块
import npack.xyz         # “dir2\npack\xyz.py”导入模块

npack.abc.func()
npack.xyz.func()
