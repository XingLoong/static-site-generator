import os
import shutil

def copy_files(dir_source, dir_destination):
  if not os.path.exists(dir_destination):
    os.mkdir(dir_destination)

  for filename in os.listdir(dir_source):
    from_path = os.path.join(dir_source, filename)
    dest_path = os.path.join(dir_destination, filename)
    print(f" * {from_path} -> {dest_path}")
    if os.path.isfile(from_path):
      shutil.copy(from_path, dest_path)
    else:
      copy_files(from_path, dest_path)