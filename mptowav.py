from os import path
#First install pydub by -
#pip install pydub (in cmd)
#sudo pip3 install pydub (in terminal)
from pydub import AudioSegment

# mp3file                                                                         
src = "justin.mp3"
#new wav file in which .wav file will be stored after converting mp3 to wav
dst = "justin.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
