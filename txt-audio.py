import os
import re
import whisper
from gtts import gTTS
 #txt to audio
#add file to project .txt file

file_path = input('Enter the txt file: ')

#regex for findig txt file
g = re.search('.txt$', file_path)

#coversion for txt to audio
if (g != None):

    f = open(file_path, "r")

z = (f.read())
speech = gTTS(z, lang="en")
#text to audio new file
speech.save("txt-audio.mp3")
print('The line ends with \'txt\'.')

# print(f"output {file_path.endswith('.txt')}")

if os.path.exists(file_path):
    print('The file exists')

    with open(file_path, 'r', encoding='latin1') as f:
        lines = f.readlines()


else:
    print('The specified file does NOT exist')
