from pytube import YouTube
import os


yt = YouTube('https://www.youtube.com/watch?v=YGHXjZlHVoI')

caption = yt.captions.get_by_language_code('ru')
subs = caption.generate_srt_captions()


file = open("subs.odf", "w")
file.write(repr(subs))
file.close()



print(subs)
