import os
from PIL import Image
import io

def save_image(image_data, output_directory):
    try:
        # Skriv ut de første 100 byte av bildedata for feilsøking
        print(image_data[:100])

        # Åpne bildestrømmen fra minnet
        image = Image.open(io.BytesIO(image_data))

        # Konstruer en filsti for å lagre bildet
        file_path = os.path.join(output_directory, 'my_image.tiff')

        # Lagre bildet
        image.save(file_path)
    except Exception as e:
        print("Feil under lagring av bildet:", e)
