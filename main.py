import cv2
from ultralytics import YOLO

# Kendi eğittiğimiz modeli yüklüyoruz (Klasör adının train2 veya train3 olup olmadığını kontrol et)
model = YOLO('runs/detect/train-2/weights/best.pt')
# Ubuntu'da varsayılan kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kameraya bağlanılamadı!")
    exit()

print("Kamera açıldı! Telefondan bir dur levhası gösterin. Çıkmak için 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kameradan görüntü okunamadı!")
        break

    # Kameradan gelen görüntüyü modele veriyoruz
    # Sadece güven puanı 0.70'in üzerindeki tespitleri göster
    results = model(frame, conf=0.70)

    # Modelin çizdiği kutuları (bounding box) resmin üzerine ekliyoruz
    annotated_frame = results[0].plot()

    # Görüntüyü ekranda gösteriyoruz
    cv2.imshow('Dur Levhasi Tespiti - Kendi Modelim', annotated_frame)

    # Klavyeden 'q' tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()