import os
from detect_watermark import *
from insert_watermark import *
from remove_watermark import *
from measure_diff import *
from poison_image import *
from merge_chunks import main as merge_parts

if not os.path.exists('merged_file.tar'):
    merge_parts()

__all__ = ['detect_watermark', 'insert_watermark', 'remove_watermark', 'measure_diff', 'poison_image']