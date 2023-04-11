from pyrogram import Client, filters
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

app = Client("my_bot", api_id=os.getenv('API_ID'),
                api_hash=os.getenv('API_HASH'), bot_token=os.getenv('BOT_TOKEN'))

@app.on_message(filters.command(["command"]) & filters.user(1089528685))
def run_command(client, message):
    command = message.text.split(maxsplit=1)[1]
    try:
        output = subprocess.check_output(
        command, shell=True, cwd="/").decode("utf-8")
        client.send_message(chat_id=message.chat.id, text=output)
    except subprocess.CalledProcessError as e:
        # If the command exits with a non-zero exit code,
        # send an error message back to the user
        client.send_message(chat_id=message.chat.id, text=f"Error: {e}")
app.run()
