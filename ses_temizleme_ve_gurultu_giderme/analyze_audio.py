import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os

dosyalar = ["oda.wav", "kafe.wav", "sokak.wav"]

for dosya in dosyalar:
    if not os.path.exists(dosya):
        print(f"Hata: Dosya bulunamadı: {dosya}")
        continue

    try:
        data, samplerate = sf.read(dosya)
        if len(data.shape) > 1:
            data = data[:, 0]

        n = len(data)
        freq = np.fft.rfftfreq(n, d=1/samplerate)
        fft_magnitude = np.abs(np.fft.rfft(data))

        plt.figure(figsize=(10, 5))
        plt.plot(freq, fft_magnitude)
        plt.title(f"Frekans Spektrumu - {dosya}")
        plt.xlabel("Frekans (Hz)")
        plt.ylabel("Genlik")
        plt.xlim(0, 8000)
        plt.grid()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"{dosya} için hata oluştu: {e}")
