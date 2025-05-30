import sounddevice as sd
import soundfile as sf

def record_audio(filename, duration, samplerate=44100):
    print("Kayıt başladı...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, audio, samplerate)
    print(f"Dosya kaydedildi: {filename}")


record_audio("oda.wav", duration=5)
 