# Python program to extract audio from video

import moviepy.editor as mp

# insert Local video File Path
clip = mp.VideoFileClip(r"did.mp4")

#Insert Local Audio File Path
clip.audio.write_audiofile(r"Audio.mp3")