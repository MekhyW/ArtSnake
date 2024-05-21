import os, site, subprocess, zipfile, shutil

def unzip_and_copy(zip_file_path, destination_directory):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        destination_path = f"{destination_directory}"
        zip_ref.extractall(destination_path)
    print(f"All files from {zip_file_path} have been copied to {destination_path}")

site_packages_dir = site.getusersitepackages()
clone_path = os.path.join(site_packages_dir, 'ArtSnake', 'deep-blind-watermark-removal')
zip_path = os.path.join(site_packages_dir, 'ArtSnake')

if os.path.exists(zip_path):
    shutil.rmtree(zip_path)

os.makedirs(clone_path, exist_ok=True)
subprocess.run(['git', 'clone', 'https://github.com/vinthony/deep-blind-watermark-removal.git', clone_path])
unzip_and_copy('ArtSnake.zip', zip_path)