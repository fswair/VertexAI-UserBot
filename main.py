from pyrogram import Client, filters, enums
from pyrogram.types import Message
from utils import VertexAI

API_ID = None
API_HASH =  None

app = Client("userbot", api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start"))
def start(client: Client, message):
    message.reply_text("Hello World!")

@app.on_message(filters.command("ask", prefixes="!"))
async def ask(client: Client, message: Message):
    ai = VertexAI()
    if message.reply_to_message:
        prompt = message.reply_to_message.text
    else:
        prompt = message.text.removeprefix("!ask").strip()
    response = ai.ask(prompt)
    if not response.startswith("```"):
        response = "```\n{}\n```".format(response)
    ai.display()
    return await message.edit("**Prompt:**\n```\n{}\n```\n**AI Response:**\n{}".format(prompt, response), parse_mode=enums.ParseMode.MARKDOWN)

app.run()
