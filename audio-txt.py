import os
import re
import whisper
#audio to text
#add file to project .wav file
file_path = input('Enter the .wav path: ')
#regex for finding the .xav file
x = re.search('.wav$', file_path)

#conversion for audio to txt (.wan file)
if (x != None):
    model = whisper.load_model("base")
    result = model.transcribe(file_path, fp16=False)
    print(result["text"])

    print('The line ends with \'wav\'.')



# print(f"output {file_path.endswith('.txt')}")

if os.path.exists(file_path):
    print('The file exists')

    with open(file_path, 'r', encoding='latin1') as f:
        lines = f.readlines()


else:
    print('The specified file does NOT exist')