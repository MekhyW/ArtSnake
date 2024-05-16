import os
from .detect_watermark import *
from .insert_watermark import *
from .remove_watermark import *
from .measure_diff import *
from .poison_image import *
from .merge_chunks import main as merge_parts
import subprocess
import site, os

if not os.path.exists('merged_file.tar'):
    merge_parts()

if not os.path.exists('deep-blind-watermark-removal'):
    site_packages_dir = site.getsitepackages()[0]
    clone_path = os.path.join(site_packages_dir, 'ArtSnake', 'deep-blind-watermark-removal')
    os.makedirs(clone_path, exist_ok=True)
    subprocess.run(['git', 'clone', 'https://github.com/vinthony/deep-blind-watermark-removal.git', clone_path])

__all__ = ['detect_watermark', 'insert_watermark', 'remove_watermark', 'measure_diff', 'poison_image']