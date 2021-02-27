# Generate Random Captcha In Python

# import required modules
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import random

# Create an instance of ImageCaptcha.
img = ImageCaptcha()
# Create an instance of AudioCaptcha.
audio = AudioCaptcha()

# generate rand string of number
rand = str(random.randint(10000, 99999))

# Call img.generate method to create the image object
img.generate(rand)
# Call img.write method to save the image to a file.
img.write(rand, 'cap.png')

# Generate autio captcha data
audio.generate(rand)
# Save the audio captcha data into a audio file.
audio.write(rand, 'aud.wav')
