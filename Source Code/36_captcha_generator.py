from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import random

img = ImageCaptcha()
audio = AudioCaptcha()

rand = str(random.randint(10000, 99999))

img.generate(rand)
img.write(rand, 'cap.png')

audio.generate(rand)
audio.write(rand, 'aud.wav')
