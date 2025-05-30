# Gürültü Giderme ve Ses Temizleme Sistemi

Bu proje, Sinyaller ve Sistemler dersi kapsamında gerçekleştirilmiş olup, farklı ortamlarda kaydedilen seslerden ortam gürültüsünü, frekans domaini analizleri ve filtreleme yöntemleriyle ayıklamayı hedeflemektedir.

## Proje İçeriği

- `record_audio.py` : Mikrofon kullanarak ses kaydı yapar.
- `analyze_audio.py` : Kayıtların frekans analizini yapar ve spektrum grafiğini çizer.
- `noise_reduce_filter.py` : NoiseReduce kütüphanesiyle sesleri temizler ve yeni dosyalar oluşturur.
- `realtime_filter.py` : Gerçek zamanlı ses filtresi uygular.
- `oda.wav`, `kafe.wav`, `sokak.wav` : Kayıt alınan ham ses dosyaları.
- `clean_*.wav` : Kayıtların temizlenmiş versiyonları.

---

## Projenin Çalıştırılması

1. **Ortam Seslerini Kaydetme**  
   Mikrofonla farklı ortamlarda ses kaydetmek için `record_audio.py` dosyasını çalıştırılır.

2. **Frekans Analizi**  
   Kayıt edilen dosyaların spektrumlarını görmek için `analyze_audio.py` dosyasını çalıştırılır. Spektrum grafikleri gösterilecektir.

3. **Ses Temizleme**  
   Gürültü azaltmak için `noise_reduce_filter.py` dosyası çalıştırılır. Temizlenmiş ses dosyaları otomatik olarak oluşturulacaktır.

4. **Gerçek Zamanlı Filtreleme**  
   Mikrofon girişini anlık işlemek ve gürültüyü bastırmak için `realtime_filter.py` dosyasını çalıştırılır. Başlıkta `Filtre çalışıyor...` mesajı görüldüğünde sistem çalışmaya başlamış demektir.

---

## Gereksinimler

- Python 3.8+
- Gerekli kütüphaneler: pip install numpy scipy matplotlib soundfile sounddevice noisereduce

## Notlar
---

## Hazırlayan

- Nagihan Zan - 22060682

---
