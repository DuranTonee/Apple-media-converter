# ffmpeg is required
import subprocess
from PIL import Image
import pyheif
import os


def convert_mov_to_mp4(input_file, output_file):
    subprocess.call(['ffmpeg', '-i', input_file, output_file])


# .heic -> .jpg, .mov -> .mp4
def converter():
    files = sorted(os.listdir("files_to_convert"))
    for file in files:
        filename, extension = os.path.splitext(file)

        if extension.lower() == ".heic":
            heic_file_path = os.path.join("files_to_convert", file)
            jpg_file_path = os.path.join("converted_files", f"{filename}.jpg")
            heif_image = pyheif.read(heic_file_path)
            image = Image.frombytes(
                heif_image.mode, 
                heif_image.size, 
                heif_image.data,
                "raw",
                heif_image.mode,
                heif_image.stride,
            )
            image.save(jpg_file_path, "JPEG")
            image.close()
            print(f"{filename} done!")

        if extension.lower() == ".mov":
            mov_file_path = os.path.join("files_to_convert", file)
            mp4_file_path = os.path.join("converted_files", f"{filename}.mp4")
            convert_mov_to_mp4(mov_file_path, mp4_file_path)
            print(f"{filename} done!")


converter()