import cv2
from PIL import Image

def capture_image():
  cap = cv2.VideoCapture(0)

  if not cap.isOpened():
    raise RuntimeError("Gagal membuka webcam.")

  print("Tekan 'SPACE' untuk mengambil gambar, atau 'ESC' untuk keluar.")

  while True:
    ret, frame = cap.read()
    if not ret:
      continue

    cv2.imshow("Webcam - Tekan SPACE untuk capture", frame)
    key = cv2.waitKey(1)

    if key == 27:  # ESC
      print("Dibatalkan.")
      cap.release()
      cv2.destroyAllWindows()
      exit()

    elif key == 32:  # SPACE
      img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      cap.release()
      cv2.destroyAllWindows()
      return Image.fromarray(img_rgb)
