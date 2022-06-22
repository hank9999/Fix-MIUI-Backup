# Fix-MIUI-Backup
Fix rollback MIUI version backup restore failed
修复降级 MIUI 后备份恢复失败的问题

## 运行 exe 版本 (仅限64Bit环境)
1. 方法一 将 `descript.xml` 文件 放在与 `Xiaomi XML Process.exe` 程序同目录下 CMD 执行 `"Xiaomi XML Process.exe" descript.xml` (powershell 运行`.\"Xiaomi XML Process.exe" descript.xml`)
2. 方法二 直接将文件拖拽到 `Xiaomi XML Process.exe` 程序上

## 运行 Python 脚本
### 安装支持库
`pip install xmltodict dicttoxml`
### 运行
py "Xiaomi XML Process.py" descript.xml
