import os
import shutil
folder = "C:/Users/chara/Downloads"
open_files = os.listdir(folder)
new_folder = os.path.join(folder,"DOC's")
os.makedirs(new_folder, exist_ok=True)
folder2 = "C:/Users/chara/Downloads/DOC's"
insert_file = "01 - Needa Padadhani.lrc"
actual_path = os.path.join(folder,insert_file)
destination = os.path.join(new_folder,insert_file)
dest_check = os.path.join(folder2,insert_file)
if os.path.exists(actual_path) and os.path.isfile(actual_path):
    shutil.move(actual_path,destination)
    print("done")
elif os.path.isfile(dest_check):
    print("already there")
else:
    print("not ok")
