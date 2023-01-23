from deepgram import Deepgram
import asyncio, json

DEEPGRAM_API_KEY = 'a57564e5cfb8c2a1b764b123668c3da91811f9a7'

PATH_TO_FILE = (r"C:\Users\belen\Desktop\Investigacion_NLP\Verbos_psicológicos\Audio_prueba.m4a")

async def main():
  # Lanzar el Deepgram SDK
  dg_client = Deepgram(DEEPGRAM_API_KEY)
  # Abre el archivo
  with open(PATH_TO_FILE, 'rb') as audio:
    # Reemplazar el mimetype como sea necesario
    source = {'buffer': audio, 'mimetype': 'audio/mp3'}
    response = await dg_client.transcription.prerecorded(source, { 'language': 'es', 'punctuate': True })
    print(json.dumps(response, indent=4))

asyncio.run(main())