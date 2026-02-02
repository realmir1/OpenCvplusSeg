# 🖼️ OpenCV ile Temel Görüntü Segmentasyonu

Bu proje, **OpenCV** kullanılarak klasik görüntü işleme yöntemleriyle
bir görüntüdeki nesnelerin arka plandan ayrılmasını (**segmentasyon**) amaçlar.

Proje, bilgisayarlı görüye yeni başlayanlar için
**temel ama güçlü bir segmentasyon örneği** sunar.

---

## 🚀 Kullanılan Yöntemler

Projede aşağıdaki görüntü işleme adımları uygulanmıştır:

- Görüntünün okunması ve yeniden boyutlandırılması  
- Gri seviye dönüşümü  
- Gaussian Blur ile gürültü azaltma  
- Otsu Threshold ile ikili segmentasyon  
- Morphological Opening ile maske temizleme  
- Contour (kontur) tespiti  
- Segment edilen nesnelerin çizilmesi  

---

## 🧠 Proje Akış Diyagramı

1. Görüntüyü oku  
2. Griye çevir  
3. Gürültüyü azalt  
4. Threshold uygula  
5. Morfolojik işlemler  
6. Nesneleri (contour) tespit et  
7. Segmentasyonu görselleştir  

---

## 🛠️ Gereksinimler

Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekir:

```bash
pip install opencv-python numpy
