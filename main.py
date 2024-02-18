import moviepy.editor as mp
import speech_recognition as sr


def video_to_text(video_path, output_text_path):
    try:
        video = mp.VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile("temp_audio.wav")

        recognizer = sr.Recognizer()
        with sr.AudioFile("temp_audio.wav") as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data, language="en-US")

        with open(output_text_path, "w") as text_file:
            text_file.write(text)

        print("Распознавание речи завершено. Результат сохранен в", output_text_path)

    except sr.UnknownValueError:
        print("Не удалось распознать речь в видео.")
    except Exception as e:
        print("Произошла ошибка:", e)


# Пример использования
video_path = input("Введите путь к видеофайлу или ссылку на YouTube: ")
output_text_path = input("Введите путь для сохранения текстового файла: ")

video_to_text(video_path, output_text_path)