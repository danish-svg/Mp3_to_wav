from os import path
from pydub import AudioSegment

# files                                                                         
src = "justin.mp3"
dst = "justin.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")