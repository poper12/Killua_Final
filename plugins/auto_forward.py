from pyrogram import Client, filters
from pyrogram.types import Message
import re

# Default for auto-forward
SOURCE_CHANNEL_ID = -1002053608688  # Update this
DESTINATION_CHANNEL_ID = -1002773214491  # Update this

# Store per-user config temporarily in memory (you can replace with DB)
user_config = {}

# ========== Auto Forwarding New Posts ==========
@Client.on_message(filters.channel & filters.chat(SOURCE_CHANNEL_ID))
async def auto_forward(client, message: Message):
    try:
        await message.copy(DESTINATION_CHANNEL_ID)
    except Exception as e:
        print(f"Error forwarding message {message.id}: {e}")

# ========== Command to Set Manual Source & Destination ==========
@Client.on_message(filters.command("set_forward_config") & filters.private)
async def set_forward_config(client, message: Message):
    args = message.text.split()
    if len(args) != 3:
        return await message.reply("Usage: `/set_forward_config source_id destination_id`", quote=True)

    try:
        src = int(args[1])
        dst = int(args[2])
        user_config[message.from_user.id] = {"source": src, "dest": dst}
        await message.reply(f"✅ Config set:\nSource: `{src}`\nDestination: `{dst}`")
    except Exception as e:
        await message.reply(f"⚠️ Error: {e}")

# ========== Manual Command to Forward Old Posts ==========
@Client.on_message(filters.command("forward_old") & filters.private)
async def forward_old(client, message: Message):
    args = message.text.split()
    if len(args) < 3:
        return await message.reply("Usage:\n`/forward_old start_id end_id`\nor\n`/forward_old https://t.me/c/ID/100 https://t.me/c/ID/110`", quote=True)

    def extract_id(x):
        match = re.search(r'/(\d+)$', x)
        return int(match.group(1)) if match else int(x)

    try:
        start_id = extract_id(args[1])
        end_id = extract_id(args[2])

        if start_id > end_id:
            return await message.reply("⚠️ Start ID must be less than or equal to End ID.")

        # Get user config or fallback to defaults
        user_id = message.from_user.id
        config = user_config.get(user_id, {"source": SOURCE_CHANNEL_ID, "dest": DESTINATION_CHANNEL_ID})
        src = config["source"]
        dst = config["dest"]

        await message.reply(f"🔄 Forwarding messages from `{start_id}` to `{end_id}`\nFrom `{src}` → `{dst}`")

        for msg_id in range(start_id, end_id + 1):
            try:
                msg = await client.get_messages(src, msg_id)
                await msg.copy(dst)
            except Exception as e:
                print(f"Failed to forward message {msg_id}: {e}")

        await message.reply("✅ Done forwarding old posts.")

    except Exception as e:
        await message.reply(f"⚠️ Error: {e}")

