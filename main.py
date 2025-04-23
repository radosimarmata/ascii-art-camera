from src.camera import capture_image
from src.converter import image_to_ascii
from src.display import show_ascii
from datetime import datetime
import os

def main():
  print("Mengambil gambar dari webcam...")
  image = capture_image()

  print("Mengubah gambar ke ASCII...")
  ascii_art = image_to_ascii(image, width=100)

  print("Menampilkan hasil di terminal...\n")
  show_ascii(ascii_art)

  # Simpan ke file
  os.makedirs("output", exist_ok=True)
  filename = f"output/ascii_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
  with open(filename, "w") as f:
    f.write(ascii_art)

  print(f"\n ASCII disimpan ke: {filename}")

if __name__ == "__main__":
  main()
