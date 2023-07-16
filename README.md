# text-wrapper
使用 text-wrapper 可以为您的文本自动逐行添加前后缀。

## 功能演示
若 `prefix = 'prefix '`，`suffix = ' suffix'`。假设 `input.txt` 文件中的内容如下：
```
apple
banana
cherry
```
运行脚本后，`output.txt` 文件中的内容将变为：
```
prefix apple suffix
prefix banana suffix
prefix cherry suffix
```
每一行前面都添加了一个前缀，后面都添加了一个后缀。

## 运行条件
请确保您的系统上安装了 Python 3.6 或更高版本。

## 使用方法
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 修改脚本中的 `prefix` 和 `suffix` 变量，以指定添加的前缀和后缀，留空为不添加。
3. 修改 `start.command (Mac)` 或 `start.bat (Win)` 中的路径，以指向您存放 `text-wrapper.py` 脚本的目录。
4. 将要处理的文本保存为 `input.txt` 文件，并放在与脚本相同的目录中。
5. 双击运行 `start.command` 或 `start.bat` 脚本以执行 `text-wrapper.py` 脚本。
6. 结果将写入到同一目录下名为 `output.txt` 的文件中。
<br>
<br>

# text-wrapper
With text-wrapper, you can automatically add a prefix and suffix to each line of your text file.

## Demo
If `prefix = 'prefix '`, `suffix = ' suffix'`. Assuming the contents of the `input.txt` file are as follows:
```
apple
banana
cherry
```
After running the script, the content of the `output.txt` file will be:
```
prefix apple suffix
prefix banana suffix
prefix cherry suffix
```
A prefix is added before each line, and a suffix is added after each line.

## Requirements
Make sure you have Python 3.6 or higher installed on your system.

## Usage
1. Clone or download the repository to a directory on your computer.
2. Modify the `prefix` and `suffix` variables in the script to specify the prefix and suffix to be added, leave blank for no addition.
3. Modify the path in `start.command (Mac)` or `start.bat (Win)` to point to the directory where you store the `text-wrapper.py` script.
4. Save the text to be processed as an `input.txt` file and place it in the same directory as the script.
5. Double-click `start.command` or `start.bat` to execute the `text-wrapper.py` script.
6. The result will be written to a file named `output.txt` in the same directory.
