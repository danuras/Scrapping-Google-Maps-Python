import cv2

def save_last_frame(video_path, output_image_path):
    # Membuka video
    cap = cv2.VideoCapture(video_path)

    # Memeriksa apakah video terbuka
    if not cap.isOpened():
        print("Error: Tidak dapat membuka video.")
        return

    last_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        last_frame = frame

    # Menyimpan frame sebagai gambar
    cv2.imwrite(output_image_path, last_frame)

    # Melepaskan objek video
    cap.release()
    print(f"Frame terakhir berhasil disimpan sebagai {output_image_path}")

# Contoh penggunaan
video_path = '..\\Promosi\\trailer\\5_2.mp4'
output_image_path = '..\\Promosi\\trailer\\5_2.jpg'
save_last_frame(video_path, output_image_path)