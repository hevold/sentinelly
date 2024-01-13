# Importer nødvendige moduler
import config
import csv_reader
import api_client
import os
import image_processor
import folder_watcher

OUTPUT_DIRECTORY = '/Users/henrikvo/Desktop/Sentinel_output'

def handle_new_csv(file_path):
    data = csv_reader.read_csv(file_path)

    for row in data:
        try:
            # Anta at første kolonne er navn, deretter lat og lon
            name, lat, lon = row
            image = api_client.get_image((lat, lon))

            if image is not None:
                file_name = f"{name}.tiff"
                file_path = os.path.join(OUTPUT_DIRECTORY, file_name)
                with open(file_path, 'wb') as file:
                    file.write(image)
                print(f"Bilde lagret som {file_path}")
            else:
                print(f"Ingen bildedata mottatt for {name}")
        except ValueError:
            print(f"Feil format i raden: {row}")

if __name__ == "__main__":
    # Start mappeovervåkningen
    folder_watcher.start_watching('/Users/henrikvo/Desktop/Kartmaskinen', handle_new_csv)
