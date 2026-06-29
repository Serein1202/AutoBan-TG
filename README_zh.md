# Telegram AutoBan

> 自动化屏蔽 Telegram 私信的轻量级工具。

Telegram AutoBan 是一个基于 **Python** 和 **Telethon** 构建的 **Telegram 用户机器人（Userbot）**。

它监控你 Telegram 账号收到的私信，并自动完成以下操作：

* 馃毇 封禁发送者
* 馃棏 删除对话
* 馃摑 记录到 ban.log

专为想要彻底屏蔽私信骚扰的用户设计。

---

[\[English\]](README.md)

---

## 功能特点

* 🚫 自动封禁陌生用户
* 🗑 封禁后自动删除对话
* 📝 记录每次封禁行为
* ✅ 支持白名单
* 👤 忽略自己的账号
* 📱 忽略通讯录联系人
* 🔒 忽略 Telegram 官方账号（777000）
* 💻 跨平台运行（Windows / Linux / macOS）

---

## 环境要求

* Python 3.9+
* Telegram 账号
* Telegram API ID
* Telegram API Hash

---

## 安装

### 克隆仓库

```bash
git clone https://github.com/Serein1202/AutoBan-TG.git

cd AutoBan-TG
```

---

### 安装依赖

```bash
pip install -r requirements.txt
```

---

## 获取 Telegram API 凭证

Telegram AutoBan **不使用 Bot Token**。

它通过 Telegram 官方 API 使用你自己的 Telegram 账号进行认证。

### 第一步

访问：https://my.telegram.org

使用你的 Telegram 账号登录。

---

### 第二步

打开：

```
API Development Tools
```

---

### 第三步

创建一个新的应用。

示例：

| 字段        | 值              |
| ---------- | ---------------- |
| App title  | Telegram AutoBan |
| Short name | autoban          |
| Platform   | Desktop          |

---

### 第四步

Telegram 会生成 API_ID 和 API_HASH，请妥善保存这两个值。

---

## 配置

复制示例配置文件：

Linux / macOS：

```bash
cp .env.example .env
```

Windows：

```bat
copy .env.example .env
```

编辑 .env：

```env
API_ID=12345678
API_HASH=0123456789abcdef0123456789abcdef
```

---

## 首次登录

运行：

```bash
python autoban.py
```

首次启动时，Telethon 会依次询问手机号（格式：+8613812345678），Telegram 会发送验证码。如果开启了两步验证，还需要输入密码。

登录成功后，会自动创建会话文件 autoban.session，只需登录一次，之后自动复用。

---

## 运行

启动 AutoBan：

```bash
python autoban.py
```

程序将持续运行，直到你手动停止。每当有人向你发送私信，AutoBan 会：记录消息、封禁发送者、删除对话。

---

## 白名单

白名单内的用户不会被封禁。

```python
WHITE_LIST = {
    777000,
    123456789,
}
```

如何获取他人的 Telegram ID：在消息处理函数中临时添加 print(sender.id)。

---

## 日志

每次封禁都会被记录到 ban.log，示例如下：

```
========== 2026-06-29 18:05:17 ==========
ID          : 123456789
Name        : John Smith
Username    : @johnsmith
Premium     : False
Bot         : False
Message     : Hello!
=========================================
```

---

## 项目结构

```
AutoBan-TG/
├── autoban.py
├── requirements.txt
├── .env.example
├── README.md
├── README_zh.md
├── LICENSE
├── .gitignore

├── autoban.session     # 首次登录后自动生成
└── ban.log             # 自动生成
```

---

## requirements.txt

```	ext
telethon>=1.41.0
python-dotenv>=1.0.0
```

---

## .env.example

```env
API_ID=
API_HASH=
```

---

## .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual Environment
.venv/
venv/
env/

# Environment Variables
.env

# Telethon Session
*.session
*.session-journal

# Logs
ban.log

# IDE
.vscode/
.idea/

# macOS
.DS_Store

# Windows
Thumbs.db
```

---

## 常见问题

### 这个项目使用 Telegram 机器人吗？

不。本项目通过 Telethon（Userbot）使用你自己的 Telegram 账号进行操作。

---

### 每次运行都需要登录吗？

不需要。首次登录成功后，Telethon 会创建本地会话文件（autoban.session），之后自动复用。

---

### 可以在 VPS 上运行吗？

可以。AutoBan 可以在 VPS、树莓派、Docker、NAS、家庭服务器、常开电脑等设备上运行。

---

## 安全提示

你的 .session 文件是你已认证的 Telegram 会话。**请勿上传或分享。**

如果会话泄露：
1. 打开 Telegram
2. 进入设置 → 设备
3. 终止对应会话
4. 删除本地 .session 文件
5. 重新登录

---

## 免责声明

本项目仅供教育和个人自动化用途。请负责任地使用，并遵守 Telegram 服务条款。作者不对因滥用而导致的账号限制或其他后果承担责任。

---

## 许可证

本项目基于 MIT 许可证开源。
