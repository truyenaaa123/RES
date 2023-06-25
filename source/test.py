import os

folder_path = "/Users/truyen/Desktop/tft/RES/texture/icon"

# Lặp qua tất cả các file trong thư mục
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Chỉ đổi tên các file, không đổi tên các thư mục con
        new_filename = filename.capitalize()  # Chuyển đổi chữ đầu in hoa
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
