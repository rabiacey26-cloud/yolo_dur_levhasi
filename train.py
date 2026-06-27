from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt') 
    print("Kendi modelimizin eğitimi başlıyor...")
    
    model.train(
        data='dataset/data.yaml', 
        epochs=15,                  
        imgsz=320,    # 1. ÇÖZÜM: RAM tasarrufu için resim boyutunu yarıya indirdik
        batch=4,      # 2. ÇÖZÜM: Yapay zekaya resimleri 16'şarlı değil, 4'erli veriyoruz
        device='cpu'                
    )
    print("Eğitim tamamlandı! Yeni model 'runs/detect/train/weights/best.pt' yoluna kaydedildi.")

if __name__ == '__main__':
    main()