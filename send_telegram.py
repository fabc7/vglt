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

def get_file_size_mb(file_path):
    size_bytes = os.path.getsize(file_path)
    return round(size_bytes / (1024 * 1024), 2)

async def main():
    try:
        if not os.path.exists(FILE_PATH):
            print(f"Error: El archivo {FILE_PATH} no existe.")
            sys.exit(1)
        
        file_size = os.path.getsize(FILE_PATH)
        if file_size == 0:
            print(f"Error: El archivo {FILE_PATH} está vacío.")
            sys.exit(1)
        
        file_size_mb = get_file_size_mb(FILE_PATH)
        
        async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
            print(f"Subiendo archivo a Telegram: {FILE_PATH} ({file_size_mb} MB)...")
            
            caption_text = (
                f"🎧 **{TITLE}**\n"
                f"🆔 ID de Emisión: `{STREAM_ID}`\n"
                f"📦 Peso: `{file_size_mb} MB`"
            )
            
            try:
                await client.send_file(
                    CANAL_ID, 
                    FILE_PATH,
                    caption=caption_text,
                    parse_mode='md',
                    attributes=[DocumentAttributeAudio(duration=0, title=TITLE)]
                )
                print(f"✓ Archivo enviado correctamente a Telegram.")
            except Exception as e:
                print(f"Error al enviar archivo a Telegram: {e}")
                sys.exit(1)
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
