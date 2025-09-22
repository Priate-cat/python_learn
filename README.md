# 图片灰度化与二值化演示

## 功能简介
- 支持上传图片或选择内置模板图片进行灰度化与自适应二值化处理
- 可调节二值化阈值，实时查看灰度图和二值图效果
- 模板图片可一键选择作为输入

## 安装与环境配置

### 1. 克隆项目
```bash
git clone https://github.com/Priate-cat/python_learn.git
cd python_learn
```

### 2. 安装依赖

推荐使用 [uv](https://github.com/astral-sh/uv)（更快的 Python 包管理器）：
```bash
uv sync
```

或使用 pip：
```bash
pip install -r requirements.txt
```

### 3. 运行项目
```bash
uv run main.py
```
或
```bash
python main.py
```

## 目录结构
```
main.py                # 主程序
requirements.txt       # 依赖包列表
pyproject.toml         # Python 项目配置
README.md              # 项目说明文档
template/              # 模板图片目录
    Lena.png
    opencv_log.png
```

## 说明
- 需提前准备好 template 目录下的模板图片。
- 推荐使用 Python 3.12 及以上版本。
- 如遇依赖问题，优先使用 uv sync。
