import os, site, subprocess

site_packages_dir = site.getsitepackages()[0]
clone_path = os.path.join(site_packages_dir, 'ArtSnake', 'deep-blind-watermark-removal')
os.makedirs(clone_path, exist_ok=True)
subprocess.run(['git', 'clone', 'https://github.com/vinthony/deep-blind-watermark-removal.git', clone_path])