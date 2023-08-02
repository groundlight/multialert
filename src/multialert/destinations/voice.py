from functools import lru_cache

from gtts import gTTS

AUDIO_CACHE_DIR = ".voice"

@lru_cache(1000)
def get_voice_audio(msg: str) -> str:
    """Returns the filename of an audio file with the given message.
    Uses TTS (text-to-speech) to generate one if not there.
    """
    audio_file = msg.replace(" ", "_")
    gTTS(msg).save(f"{AUDIO_CACHE_DIR}/{audio_file}.mp3")
    return audio_file
