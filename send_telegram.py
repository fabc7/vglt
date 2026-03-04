import os
import sys
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import DocumentAttributeAudio

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]
CANAL_ID = int(os.environ["CANAL_ID"])

FILE_PATH = sys.argv[1]
TITLE = sys.argv[2] if len(sys.argv) > 2 else "Grabación de Twitch"
STREAM_ID = sys.argv[3] if len(sys.argv) > 3 else "N/A"

async def main():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print(f"Error: El archivo {FILE_PATH} no existe o está vacío.")
        sys.exit(1)
        
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        print(f"Subiendo archivo a Telegram: {FILE_PATH}...")
        
        caption_text = f"🎧 **{TITLE}**\n🆔 ID del Stream: `{STREAM_ID}`"
        
        await client.send_file(
            CANAL_ID, 
            FILE_PATH,
            caption=caption_text,
            parse_mode='md', # Esto permite usar negritas y formato código
            attributes=[DocumentAttributeAudio(duration=0, title=TITLE)]
        )
        print(f"Archivo enviado correctamente: {FILE_PATH}")

if __name__ == "__main__":
    asyncio.run(main())
