import speech_recognition as sr
import sys

r = sr.Recognizer()

filename = sys.argv[1]
# with sr.Microphone() as source:
#     print("Say Something ---")
#     audio = r.listen(source)
#     print("Done")

with sr.AudioFile(filename) as source:
    audio = r.listen(source)

# text = r.recognize_google(audio, language = 'fr-FR')
# print(text)
# language codes link -- https://cloud.google.com/speech-to-text/docs/languages
print(r.recognize_google(audio))