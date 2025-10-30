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

### 2. 虚拟环境配置

推荐使用 [uv](https://github.com/astral-sh/uv)（更快的 Python 包管理器）：
```bash
uv sync  # 自动创建虚拟环境，并安装相关依赖
```

或使用 pip（需手动创建虚拟环境）：
```bash
python -m venv .venv  # 创建虚拟环境
# source venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # 激活虚拟环境
pip install -r requirements.txt
```

或使用 conda：
```bash
conda create -n myenv python=3.12  # 创建虚拟环境
conda activate myenv  # 激活虚拟环境
conda install -r requirements.txt  # 在虚拟环境中安装第三方库
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

## 这个项目里每个文件/文件夹是干什么的

- `main.py`：这是项目的“开关”。就像玩具的开关，运行它程序就会开始工作。它会把图片变灰、再做二值化，并把结果显示出来。

- `requirements.txt`：这是一个清单，写着这个程序需要哪些外面的“魔法工具”（也就是 Python 的库）。当你运行安装命令时，电脑会根据这个清单把需要的库装好。

- `pyproject.toml`：这是给程序做说明和设置的文件。可以把它想成一本小笔记，告诉一些工具这个项目需要怎样的配置。初学者一般不用改它，只需要知道它是项目的配置文件。

- `README.md`：就是这个文件。它会告诉别人这个项目是干什么的、如何使用、以及每个文件的作用。把它当成项目的小说明书。

- `.gitignore`：这是给 Git（版本管理工具）看的规则表。它告诉 Git：有些文件我们不想上传到网上（比如你电脑里的临时文件、密码文件、或者很大的图片），就把它们忽略掉。

- `.python-version`：这个文件通常用来记住你想用哪个版本的 Python（比如 3.10、3.12）。就像写下来“我要用 3.12 运行这个程序”，方便工具知道该用哪个 Python。

- `uv.lock`：如果你用了 `uv` 来安装依赖，会生成这个锁文件。它记录下确切安装了哪些库和版本，确保别人用同样的清单装出来的环境和你的一样。可以把它想成“依赖的拍照记录”。

- `template/`（文件夹）：这里面放了演示用的图片（比如 `Lena.png`, `opencv_logo.png`, `img1.png`）。当你不想自己上传图片时，可以直接用这些模板圖片来试验程序。

  - `template/Lena.png`：一个常用的测试图片。
  - `template/opencv_logo.png`：OpenCV 的 logo 图，项目里可能用来做测试。
  - `template/img1.png`：另一个示例图片。