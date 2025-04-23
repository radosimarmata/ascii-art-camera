from PIL import Image

# Karakter ASCII diurutkan dari gelap ke terang
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
  width, height = image.size
  aspect_ratio = height / width
  new_height = int(aspect_ratio * new_width * 0.55)
  resized_image = image.resize((new_width, new_height))
  return resized_image

def grayify(image):
  return image.convert("L")  # Ubah ke grayscale

def pixels_to_ascii(image):
  pixels = image.getdata()
  ascii_str = "".join([ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels])
  return ascii_str

def image_to_ascii(image, width=100):
  image = resize_image(image, new_width=width)
  image = grayify(image)
  ascii_str = pixels_to_ascii(image)

  # Format string jadi baris-baris
  pixel_count = len(ascii_str)
  ascii_image = "\n".join(
    [ascii_str[index:(index + width)] for index in range(0, pixel_count, width)]
  )

  return ascii_image
