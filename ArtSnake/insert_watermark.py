import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import random
import os

def fit_text_in_box(font, bounding_box, text):
    x, y, w, h = bounding_box
    best_font_size = 1
    best_num_lines = float('inf')
    best_text_lines = []
    vertical_offset = 0
    for font_size in range(1, h):
        current_font = ImageFont.truetype(font, font_size)
        draw = ImageDraw.Draw(Image.new('RGB', (1, 1)))
        text_width, text_height = draw.textbbox((0, 0), text, font=current_font)[2:]
        lines = []
        line = ''
        for word in text.split():
            if draw.textbbox((0, 0), line + word, font=current_font)[2] <= w:
                line += word + ' '
            else:
                lines.append(line.strip())
                line = word + ' '
        if line:
            lines.append(line.strip())
        num_lines = len(lines)
        total_text_height = text_height * num_lines
        if total_text_height <= h and (num_lines < best_num_lines or (num_lines == best_num_lines and font_size > best_font_size)):
            best_font_size = font_size
            best_num_lines = num_lines
            best_text_lines = lines
            vertical_offset = (h - total_text_height) // 2
    return best_font_size, best_text_lines, vertical_offset

def insert_text_pass(img):
    return img

def insert_text_simple(img, text, font_path, font_size=30):
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    font_size, lines, vertical_offset = fit_text_in_box(font_path, (0, 0, pil_img.width, pil_img.height), text)
    font = ImageFont.truetype(font_path, font_size)
    x = 0
    y = (pil_img.height - font_size) // 2
    bg_color = tuple(img.mean(axis=(0, 1)).astype(int))
    text_color = (255, 255, 255) if sum(bg_color) < 383 else (0, 0, 0)
    draw.text((x, y), text, font=font, fill=text_color)
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

if __name__ == '__main__':
    font = os.path.join('fonts', random.choice(os.listdir('fonts')))
    img = cv2.imread('example.jpg')
    img1 = insert_text_pass(img)
    img2 = insert_text_simple(img, 'Lorem ipsum', font)
    cv2.imshow('insert_text_pass', img1)
    cv2.imshow('insert_text_simple', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()