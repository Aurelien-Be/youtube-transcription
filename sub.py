from pytube import YouTube
import re
import os

ytlink = input("Youtube Link:")
yt = YouTube(ytlink)


caption = yt.captions.get_by_language_code('ru')
justTextCaption = re.sub("[<].*?[>]", " ", caption.generate_srt_captions())



print(justTextCaption)


path = R'C:\Users\Asus\Documents\Transcriptions'
file = input('name of the file:')
with open(os.path.join(path, file), 'w') as text_file:
    text_file.write(justTextCaption)

