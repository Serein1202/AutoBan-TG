from telethon import TelegramClient, events
from telethon.tl.functions.contacts import BlockRequest
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

# ==========================
# 加载 .env 配置
# ==========================
load_dotenv()

# ==========================
# 开启日志（可看到 Telethon 连接情况）
# ==========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==========================
# Telegram API
# ==========================
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

# ==========================
# 白名单（不会被拉黑）
# 填 Telegram 用户 ID
# 例如：
# WHITE_LIST = {123456789, 987654321}
# ==========================
WHITE_LIST = {
    777000,     # Telegram 官方验证码账号
}

# ==========================
# 写日志
# ==========================
def write_log(sender, message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = (
        f"\n========== {now} ==========\n"
        f"ID          : {sender.id}\n"
        f"Name        : {(sender.first_name or '')} {(sender.last_name or '')}\n"
        f"Username    : @{sender.username if sender.username else 'None'}\n"
        f"Phone       : {sender.phone or 'Hidden'}\n"
        f"Premium     : {getattr(sender, 'premium', False)}\n"
        f"Bot         : {sender.bot}\n"
        f"Message     : {message}\n"
        f"====================================\n"
    )

    with open("ban.log", "a", encoding="utf-8") as f:
        f.write(log)


# ==========================
# 收到消息
# ==========================
@client.on(events.NewMessage(incoming=True))
async def on_message(event):
    try:

        # 只处理私聊
        if not event.is_private:
            return

        sender = await event.get_sender()

        # 自己
        if sender.is_self:
            return

        # 联系人
        # if sender.contact:
            # return

        # 白名单
        if sender.id in WHITE_LIST:
            return

        print("=" * 60)
        print("收到陌生人私信")
        print(f"昵称：{sender.first_name}")
        print(f"ID：{sender.id}")
        print(f"消息：{event.raw_text}")

        # 回复告知已被拉黑
        await event.reply("未经许可私聊已被ban，请通过 @Serein0504_bot 联系")

        # 写日志
        write_log(sender, event.raw_text)

        # 拉黑
        await client(BlockRequest(sender.id))

        # 删除聊天
        await client.delete_dialog(sender.id)

        print("✓ 已拉黑并删除聊天")

    except Exception as e:
        print("发生错误：", e)


# ==========================
# 启动
# ==========================
client.start()

print("=" * 60)
print("Telegram AutoBan 已启动")
print("等待陌生人私信...")
print("=" * 60)

client.run_until_disconnected()
