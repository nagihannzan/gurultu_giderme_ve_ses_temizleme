import noisereduce as nr
import soundfile as sf
import os
import numpy as np

def clean_with_nr(filename):
    if not os.path.exists(filename):
        print(f"Hata: Dosya bulunamadı: {filename}")
        return

    try:
        y, sr = sf.read(filename)
        if len(y.shape) > 1:
            y = y[:, 0]

        noise_sample = y[:int(sr * 1.0)]

        reduced_noise = nr.reduce_noise(y=y, sr=sr, y_noise=noise_sample, prop_decrease=1.2)

        output_file = filename.replace(".wav", "_clean.wav")
        sf.write(output_file, reduced_noise, sr)
        print(f"Temizlendi: {output_file}")

    except Exception as e:
        print(f"Hata oluştu ({filename}): {e}")

dosyalar = ["oda.wav", "kafe.wav", "sokak.wav"]
for dosya in dosyalar:
    clean_with_nr(dosya)
