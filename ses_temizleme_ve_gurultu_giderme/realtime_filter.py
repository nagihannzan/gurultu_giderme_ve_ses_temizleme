import numpy as np
import sounddevice as sd
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=6):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_filter(data, b, a):
    return lfilter(b, a, data)

samplerate = 44100
block_size = 1024
lowcut = 100
highcut = 4000
b, a = butter_bandpass(lowcut, highcut, samplerate)

volume_threshold = 0.003

print("Gerçek zamanlı filtre başlıyor...")

def callback(indata, outdata, frames, time, status):
    if status:
        print(f"Hata: {status}")

    audio_in = indata[:, 0]

    filtered = apply_filter(audio_in, b, a)

    mask = np.abs(filtered) < volume_threshold
    filtered[mask] *= 0.3

    outdata[:, 0] = filtered

with sd.Stream(channels=1, callback=callback, samplerate=samplerate, blocksize=block_size):
    input("Filtre çalışıyor. Bitirmek için Enter'a bas...")
