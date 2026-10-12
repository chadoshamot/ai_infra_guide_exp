# ai_infra_guide_exp

保存学习 AIInfraGuide 时对手册实验的实现。

## 第一个实验

`chap1/fast_scale(添加c++算子到python)`：通过 pybind11 给 Python 添加 C++ 逐元素缩放算子。

在 Windows PowerShell 中，使用已安装 Python、CMake 和 MinGW 的环境，进入实验目录后运行：

```powershell
python -m pip install pybind11
$pybind11Dir = python -m pybind11 --cmakedir
$pythonExe = python -c "import sys; print(sys.executable)"
cmake -S . -B build-mingw -G "MinGW Makefiles" "-Dpybind11_DIR=$pybind11Dir" "-DPython_EXECUTABLE=$pythonExe" -DCMAKE_BUILD_TYPE=Release
cmake --build build-mingw --parallel
python test_scale.py
```

预期输出：`[2.0, -4.0, 7.0]`。
