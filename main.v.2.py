import moviepy.editor as mp
import speech_recognition as sr

def video_to_text(video_path, output_text_path):
    try:
        video = mp.VideoFileClip(video_path)
        audio = video.audio
        duration = audio.duration
        recognizer = sr.Recognizer()
        text = ""
        chunk_duration = 10 * 60  # 10 minutes in seconds

        for i in range(0, int(duration), chunk_duration):
            start_time = i
            end_time = min(i + chunk_duration, duration)
            audio_chunk = audio.subclip(start_time, end_time)
            audio_chunk.write_audiofile("temp_audio.wav", codec='pcm_s16le')

            with sr.AudioFile("temp_audio.wav") as source:
                audio_data = recognizer.record(source)

            text += recognizer.recognize_google(audio_data, language="ru-RU") + "\n"

        with open(output_text_path, 'w', encoding='utf-8') as file:
            file.write(text)

        print("Распознавание речи завершено. Результат сохранен в", output_text_path)

    except sr.UnknownValueError:
        print("Не удалось распознать речь в видео.")
    except Exception as e:
        print("Произошла ошибка:", e)


# Пример использования
video_path = input("Введите путь к видеофайлу или ссылку на YouTube: ")
output_file_name = input("Введите название для сохраняемого файла: ")
output_text_path = input("Введите путь для сохранения текстового файла (включая название и расширение): ")

video_to_text(video_path, output_text_path)