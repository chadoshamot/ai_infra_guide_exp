# windows适配
import os
import shutil
import sys
from pathlib import Path

project_dir = Path(__file__).resolve().parent
mingw_bin = Path(shutil.which("g++")).parent

# 告诉 Python 去哪里寻找 MinGW 的运行库 DLL
dll_dir = os.add_dll_directory(str(mingw_bin))

# 告诉 Python 去哪里寻找编译好的扩展
sys.path.insert(0, str(project_dir / "build-mingw"))

import fast_scale

actual = fast_scale.scale([1.0, -2.0, 3.5], 2.0)
expected = [2.0, -4.0, 7.0]
assert actual == expected
print(actual)

# # 1. 安装 pybind11
# python -m pip install pybind11

# # 2. 获取当前环境路径
# $pybind11Dir = python -m pybind11 --cmakedir
# $pythonExe = python -c "import sys; print(sys.executable)"

# # 3. 使用本机已有的 MinGW 配置构建
# cmake -S . -B build-mingw -G "MinGW Makefiles" "-Dpybind11_DIR=$pybind11Dir" "-DPython_EXECUTABLE=$pythonExe" -DCMAKE_BUILD_TYPE=Release

# # 4. 编译（上一步成功后执行）
# cmake --build build-mingw --parallel

# # 5. 验证（编译成功后执行）
# python -c "import sys; sys.path.insert(0, 'build-mingw'); import fast_scale; actual = fast_scale.scale([1.0, -2.0, 3.5], 2.0); assert actual == [2.0, -4.0, 7.0]; print(actual)"