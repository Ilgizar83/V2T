import moviepy.editor as mp
import speech_recognition as sr

# Функция для конвертации видео в аудио и распознавания речи
def video_to_text(video_file):
    video = mp.VideoFileClip(video_file)
    video.audio.write_audiofile("audio.wav")

    recognizer = sr.Recognizer()
    audio = sr.AudioFile("audio.wav")

    with audio as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Распознавание речи не удалось")
            return ""

# Основная часть программы
video_file = input("Введите путь к видеофайлу или ссылку на YouTube: ")
text = video_to_text(video_file)

output_file = input("Укажите путь для сохранения текстового файла: ")
with open(output_file, "w") as file:
    file.write(text)

print("Текстовый файл успешно сохранен.")