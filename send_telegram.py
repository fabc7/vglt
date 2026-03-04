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

async def main():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print(f"Error: El archivo {FILE_PATH} no existe o está vacío.")
        sys.exit(1)
        
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        print(f"Subiendo archivo a Telegram: {FILE_PATH}...")
        await client.send_file(
            CANAL_ID, 
            FILE_PATH,
            attributes=[DocumentAttributeAudio(duration=0, title=os.path.basename(FILE_PATH))]
        )
        print(f"Archivo enviado correctamente: {FILE_PATH}")

if __name__ == "__main__":
    asyncio.run(main())
